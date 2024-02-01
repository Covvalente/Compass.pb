
primeirosNomes=['Joao','Douglas','Lucas','José']
sobreNomes=['Soares','Souza','Silveira','Pedreira']
idades = [19,28,25,31]

lista =list (zip(primeirosNomes,sobreNomes,idades))

for i, pessoa in enumerate (lista):
    print(f"{i} - {pessoa[0]} {pessoa[1]} está com {pessoa[2]} anos")