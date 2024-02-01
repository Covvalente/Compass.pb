def primo(num):
    
    if num <=1:
        return False

    for i in range (2,num+1):
        if num % i ==0 and num !=i:
         return False
    return True

for i in range (1,101):
    if primo (i):
        print (i)