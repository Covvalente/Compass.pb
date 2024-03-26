class Passaro():
    def voa (self):
        print ("Voando ...")
        
        def emite_som(self):
            print("Passaro emitindo som...")
            
class Pato(Passaro):
    _nome = "Pato"
    
    def emite_som(self):
        print ("pato emitindo som...")
        print ("Quack Quack")
        
    @property 
    def nome (self):
        return self._nome
        
class Pardal (Passaro):
    _nome = "Pardal "
    
    def emite_som (self):
        print("Pardal emitindo Som...")
        print ("Piu Piu ")
        
    @property
    def nome (self):
        return self._nome
        
    
pato = Pato()
pardal = Pardal()
    
print(pato.nome)
pato.voa()
pato.emite_som()