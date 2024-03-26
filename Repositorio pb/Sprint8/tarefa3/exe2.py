import csv 

animais = ["cachorro","gato","peixe","pássaro","coelho","cobra","elefante","girafa","macaco","leão","tigre","zebra","hipopótamo","panda","rinoceronte","tartaruga","coruja","camelo","avestruz","crocodilo"]

animais_ordenados=sorted(animais)

print ("animais em ordem decrescente")
[print(animal)for animal in reversed (animais_ordenados)]

with open ("animais.csv","w",newline="")as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for animal in animais_ordenados:
            escritor_csv.writerow([animal])
            
print("conteúdo dos animais foi salvo em animais.csv")
    