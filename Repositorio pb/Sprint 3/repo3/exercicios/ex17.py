def tres_listas(lista):
    if len(lista) %3 ==0:
        n=len(lista)//3
        l1= lista[:n]
        l2= lista[n:(n*2)]
        l3= lista[(n*2):]
        return l1,l2,l3
        
    else:
        print ("Não é possivel dividir a lista em 3 partes iguais")
        n = round (len(lista)/3)
        l1=lista[:n]
        l2=lista[n:(n*2)]
        l3=lista[(n*2):]
        return l1,l2,l3
        
lista =[1,2,3,4,5,6,7,8,9,10,11,12]

listas = tres_listas(lista)
print (listas[0], listas[1], listas[2])