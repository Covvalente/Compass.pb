import json
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Configurações
    TMDB_API_KEY = 'a173347486b652238aa1f1dd25203a94'
    oscars_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_awards=true"

    # Buscar os filmes vencedores do Oscar
    response = requests.get(oscars_url)
    data = response.json()
    filmes = data.get('results', [])

    # Encontrar o filme de romance mais premiado
    filmes_romance = [filme for filme in filmes if any(genero.get('name') == 'Romance' for genero in filme.get('genres', []))]
    if not filmes_romance:
        filme_romance_mais_premiado = None
    else:
        filme_romance_mais_premiado = max(filmes_romance, key=lambda x: x.get('vote_count', 0))

    # Extrair informações do filme escolhido
    titulo_filme = filme_romance_mais_premiado['title'] if filme_romance_mais_premiado else None
    orcamento = filme_romance_mais_premiado['budget'] if filme_romance_mais_premiado else None
    receita = filme_romance_mais_premiado['revenue'] if filme_romance_mais_premiado else None
    elenco = filme_romance_mais_premiado['cast'] if filme_romance_mais_premiado else None
    diretor = filme_romance_mais_premiado['director'] if filme_romance_mais_premiado else None
    ano_lancamento = filme_romance_mais_premiado['release_year'] if filme_romance_mais_premiado else None
    media_score = filme_romance_mais_premiado['average_score'] if filme_romance_mais_premiado else None

    # Encontrar os protagonistas masculino e feminino
    protagonista_masculino = None
    protagonista_feminino = None
    if elenco:
        atores_masculinos = [ator['name'] for ator in elenco if ator['gender'] == 2]  # 2 representa o gênero masculino
        atores_femininos = [ator['name'] for ator in elenco if ator['gender'] == 1]  # 1 representa o gênero feminino
        if atores_masculinos:
            protagonista_masculino = atores_masculinos[0]
        if atores_femininos:
            protagonista_feminino = atores_femininos[0]

    # Salvar os dados no Amazon S3
    s3 = boto3.client('s3')
    hoje = datetime.now().strftime('%Y/%m/%d')
    chave_arquivo = f"dados_filme_romance_{hoje}.json"
    s3.put_object(Body=json.dumps({
        'titulo_filme': titulo_filme,
        'orcamento': orcamento,
        'receita': receita,
        'protagonista_masculino': protagonista_masculino,
        'protagonista_feminino': protagonista_feminino,
        'diretor': diretor,
        'ano_lancamento': ano_lancamento,
        'media_score': media_score
    }), Bucket='seu-nome-do-bucket', Key=chave_arquivo)

    return {
        'statusCode': 200,
        'body': json.dumps('Dados salvos no Amazon S3 com sucesso!')
    }
