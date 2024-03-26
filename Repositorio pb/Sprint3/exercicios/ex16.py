def soma_string(string):
    lista =string.split(",")
    
    soma=0
    for i in lista:
        soma += int (i)
    return soma
    
string ="1,3,4,6,10,76"

print (soma_string(string))