class Persona:
    def __init__(self):
        self.edad = 0
        self.nombre = ""
    def setEdad(self,nuevaedad):
        if self.edad == nuevaedad - 1:
            self.edad = nuevaedad
        

Juan = Persona()
print(Juan.edad)
Juan.setEdad(1)
print(Juan.edad)
