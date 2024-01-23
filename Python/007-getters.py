class Persona:
    def __init__(self):
        self.edad = 0
        self.nombre = ""
    def setEdad(self,nuevaedad):
        if self.edad == nuevaedad - 1:
            self.edad = nuevaedad
    def getEdad(self):
        return "Mi edad es:"+str(self.edad)

Juan = Persona()
print(Juan.getEdad())
Juan.setEdad(1)
print(Juan.getEdad())
