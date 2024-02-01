class Lampada:
    ligada=False
    
    def __init__(self, ligada=False):
        self._ligada = ligada

    def liga(self):
        if not self._ligada:
            self._ligada = True

    def desliga(self):
        if self._ligada:
            self._ligada = False

    def esta_ligada(self):
        return self._ligada


lamp = Lampada(True)


lamp.liga()
print("A lâmpada está ligada? " + str(lamp.esta_ligada()))


lamp.desliga()
print("A lâmpada ainda está ligada? " + str(lamp.esta_ligada()))
