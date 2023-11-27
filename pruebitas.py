"""
class Persona:
    def __init__(self, nombre, apellido, saludo="Hola",email="hola@email.com"):
        self.nombre = nombre
        self.apellido = apellido
        self.saludo = saludo
        self.email  = email
        print("Hola esto es clase persona")

    def __repr__(self):
        return f"Nombre:{self.nombre},Apellido:{self.apellido},Saludo:{self.saludo},Email:{self.email}"

    def mostrarDatos(self):
         return f"Nombre:{self.nombre},Apellido:{self.apellido},Saludo:{self.saludo},Email:{self.email}"    

objPersona = Persona(email="pepelo@gmail.com",apellido="Lopez",saludo="Bon dia",nombre="Pepe")

print( objPersona.mostrarDatos() )
"""
import random

for i in range(1,11):
    print( random.randint(5,1000) )