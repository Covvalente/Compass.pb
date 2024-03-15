def pares_ate(n: int):
    # Certifica-se de que n seja pelo menos 2
    n = max(n, 2)

    # Itera de 2 até n (inclusive) com passo 2, gerando apenas números pares
    for i in range(2, n + 1, 2):
        yield i

# Exemplo de uso da função
n = 10
gerador = pares_ate(n)

# Itera sobre os valores gerados
for numero in gerador:
    print(numero)
