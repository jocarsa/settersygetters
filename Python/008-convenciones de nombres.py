class Persona:
    def __init__(self):
        self.__edad = 0
        self.nombre = ""
    def setEdad(self,nuevaedad):
        if self.__edad == nuevaedad - 1:
            self.__edad = nuevaedad
    def getEdad(self):
        return "Mi edad es:"+str(self.__edad)

Juan = Persona()
print(Juan.getEdad())
Juan.setEdad(1)
print(Juan.getEdad())
print(Juan.__edad)
