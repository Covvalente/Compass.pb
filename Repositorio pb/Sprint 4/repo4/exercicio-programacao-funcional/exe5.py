import csv

# extrai os dados do arquivo e joga numa lista(num)
def extrai(caminho):
    file = open(caminho, encoding="utf-8")
    num = csv.reader(file)

    # filtra e retorna os valores pedidos
    def filtra():
        # função a ser passada no map, recebe uma lista (nome e 5 notas de uma aluno) e retorna uma lista já filtrada com apenas o nome e as 3 maiores notas
        def func(x):
            # transforma as 5 notas em int
            notas = list(map(lambda x: int(x), x[1:6]))
            # ordena pela maior nota
            notas = sorted(notas, reverse=True)
            # cria lista com o nome do aluno eas 3 maiores notas
            lista = [x[0], notas[:3]]
            return lista

        # aplica a função a cada aluno da lista e oredena pelo nome do aluno
        lista = sorted(list(map(func, num)))

        # retorna o relatório textual para cada aluno
        # a média é a soma das 3 notas / pelo tamamnho da lista e arredondado pra 2 casas
        file.close()
        return list(map(lambda x: print(f"Nome: {x[0]} Notas: {x[1]} Média: {round(sum(x[1])/len(x[1]), 2)}"), lista))
    return filtra()

extrai("repo4/exercicio-programacao-funcional/estudantes.csv")