import datetime 

def ano_100(idade):
    ano_atual=datetime.datetime.now().year
    anos_para_100=100-idade
    ano_100=ano_atual+anos_para_100
    return ano_100

nome = input('Informe seu nome:')
idade =''

while type (idade) !=int:
    try:
        idade=int(input('Informe sua idade: '))
    except ValueError:
        print("Valor inválido, informe um número")
        
print (ano_100(idade))