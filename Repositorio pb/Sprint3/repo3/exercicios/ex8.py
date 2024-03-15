lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in lista:
    if i == i[::-1]:
        print("A palavra: " + i + " é um palíndromo")
    else: 
        print("A palavra: " + i + " não é um palíndromo")
