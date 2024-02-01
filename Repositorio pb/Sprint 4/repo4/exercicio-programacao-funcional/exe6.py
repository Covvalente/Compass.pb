def produtos_acima_da_media(conteudo):
    # Calcula a média dos valores
    valores = list(conteudo.values())
    media = sum(valores) / len(valores)

    # Filtra os produtos cujo valor é superior à média
    produtos_acima_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]

    # Retorna a lista ordenada pelo preço (ordem crescente)
    return sorted(produtos_acima_media, key=lambda x: x[1])

def maiores_que_media(conteudo: dict) -> list:
    return produtos_acima_da_media(conteudo)

# Exemplo de uso
conteudo_exemplo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(conteudo_exemplo)
print(resultado)
