def impar_par(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

for i in range(3):
    num = ''
    while type(num) != int:
        try:
            num = int(input(f"Informe o número {i+1}: "))
        except ValueError:
            print("Valor inválido, informe um número inteiro")

    print(f'{impar_par(num)}: {num}')
