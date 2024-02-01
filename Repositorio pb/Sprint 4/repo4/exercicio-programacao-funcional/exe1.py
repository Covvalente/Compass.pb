def extrai(caminho):
    with open(caminho) as file:
        num = file.read().split("\n")
        num = list(map(lambda x: int(x), num))
        file.close()

    def filtra():
        par = lambda x: x % 2 == 0

        # filtra(filter) somente os pares da lista, ordena(sorted) esse resultado em ordem decrescente(reverse=True) e pega somente os 5 primeiros valores([0:5])
        return list(sorted(filter(par, num), reverse=True))[0:5]
    
    return filtra()


lista = extrai("repo4/exercicio-programacao-funcional/number.txt")

print(lista)
print(sum(lista))