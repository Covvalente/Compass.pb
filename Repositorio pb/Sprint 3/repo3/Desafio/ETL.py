def extrai(): ## etapa 1 
    with open("repo3/Desafio/actors.csv", "r", encoding="utf8") as file:
        lista = []  # Lista para armazenar os dados extraídos
        contador = 0  # Contador para ignorar a primeira linha (cabeçalho)

        for line in file.readlines():
            ator = {}  # Dicionário para armazenar informações de cada ator

            if contador == 0:
                contador += 1
                continue  # Ignora o cabeçalho na primeira iteração

            item = line.split(",")

            if len(item) > 6:
                # Tratamento para casos em que o nome do ator contém vírgulas
                item_diferente = line.split('"')
                novo = item_diferente[1].replace(",", "") + item_diferente[2]
                item = novo.split(",")

                for i in item:
                    i.strip()

            # Preenche o dicionário com as informações do ator
            ator['nome'] = item[0]
            ator['total'] = float(item[1])
            ator['filmes'] = int(item[2])
            ator['media'] = float(item[3])
            ator['1 filme'] = item[4]
            ator['bruto'] = float(item[5])

            lista.append(ator)  # Adiciona o dicionário à lista

    return lista


def mais_filmes(dados):
    ator, numero = maior(dados, 'filmes')

    with open("repo3/Desafio/etapa1.txt", "w", encoding="utf-8") as file:
        file.write(" O ator/atriz com maior número de filmes e o respectivo número de filmes :\n\n ")
        file.write("Ator, Número de filmes \n")
        for nome in ator:
            file.write(f"{nome},{numero}")
    return ator, numero

##etapa 2
def media_filmes(dados):
    if not dados:
        return 0  # Retorna zero se a lista de dados estiver vazia para evitar divisão por zero
 
    soma = sum(ator['bruto'] for ator in dados)  # Soma o número de filmes de cada ator na lista
    media = soma / len(dados)  # Calcula a média
 
    # Escreve a média em um arquivo chamado "etapa2.txt"
    with open("repo3/Desafio/etapa2.txt", "w", encoding="utf-8") as file:
        file.write(f"A média do número de filmes por autor:\n\n{media}")
 
    return media  # Retorna a média calculada



# etapa 3
def maior(lista, dado):
    if not lista:
        return None, None  # Retorna None se a lista estiver vazia

    maior_valor = lista[0][dado]
    nomes = [lista[0]['nome']]

    for item in lista[1:]:
        if item[dado] > maior_valor:
            maior_valor = item[dado]
            nomes = [item['nome']]
        elif item[dado] == maior_valor:
            nomes.append(item['nome'])

    return nomes, maior_valor

def maior_media(dados):
    ator, maior_media = maior(dados, 'media')

    # Escreve no arquivo "etapa3.txt" o ator ou atriz com a maior média por filme
    with open("repo3/Desafio/etapa3.txt", "w", encoding="utf-8") as file:
        file.write(" O ator/ atriz com a maior média por filme:\n\n")
        for nome in ator:
            file.write(nome)
    
    return ator



#etapa 4 
def filme_frequente(dados):
    filmes_contagem = {}
    
    # Contagem de aparições dos filmes
    for item in dados:
        filme = item['1 filme']
        
        if filme not in filmes_contagem:
            filmes_contagem[filme] = 1
        else:
            filmes_contagem[filme] += 1

    # Ordenação dos filmes por frequência decrescente e nome do filme
    filmes_ordenados = sorted(filmes_contagem.items(), key=lambda x: (x[1], x[0]), reverse=True)

    with open("repo3/Desafio/etapa4.txt", "w", encoding="utf-8") as file:
        file.write("O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência :\n\n")
        file.write("Filme, Frequência\n")

        # Escrevendo no arquivo no formato especificado
        for sequencia, (filme, frequencia) in enumerate(filmes_ordenados, start=1):
            file.write(f"{sequencia} - O filme {filme} aparece {frequencia} vez(es) no dataset.\n")

    return filmes_ordenados




# etapa 5 

def autores_receita_bruta(dados):
    # Ordenando os atores pela receita bruta de bilheteria de seus filmes em ordem decrescente
    atores_ordenados = sorted(dados, key=lambda x: x['total'], reverse=True)

    with open("repo3/Desafio/etapa5.txt", "w", encoding="utf-8") as file:
        file.write("A lista dos Autores ordenada por pagamento, do mais bem pago para o menos bem pago:\n\n")

        # Escrevendo no arquivo no formato especificado
        for ator in atores_ordenados:
            file.write(f"{ator['nome']} - {ator['total']}\n")

    return atores_ordenados


# Extraindo dados e executando as funções
dados = extrai()
resultado_filme_frequente = filme_frequente(dados)
resultado_autores_receita_bruta = autores_receita_bruta(dados)

