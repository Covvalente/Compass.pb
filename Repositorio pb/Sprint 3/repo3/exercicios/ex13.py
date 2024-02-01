def my_map(lista,f):
    return list(map(f,lista))
    
lista= [1,2,3,4,5,6,7,8,9,10]
print (my_map(lista, lambda x:x**2))