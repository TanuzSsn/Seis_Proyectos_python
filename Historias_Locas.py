# Historias locas, basado en "Cards Against Humanity"

#Vamos a utilizar las librerias de Numpy para trabajar con arreglos/listas
# y con random para seleccionar aleatoriamente datos de estos arreglos/listas

import numpy as np
import random

#Definimos nuestra lista de frases a usar

frases = np.array([
                    "Ahora se prohíbe _____ en los aviones",
                    "Es una pena que los niños de ahora se involucren en _____",
                    "Y el oscar a _____ va para _____",
                    "El siguiente libro de J.K Rowling: Harry Potter y la Camara de _____",
                    "Disculpe Maestro, no acabé la tarea porque hubo _____",
                    "_____ + _____ = _____ . ",
                  ])

#Declaramos las palabras que podemos usar

palabras = np.array(["Fuego Amigo", 
                     "Ernesto Zedillo", 
                     "Una Maldicion Gitana", 
                     "Viboras Voladoras Sexuales",
                     "Hambruna",
                     "Estrellas porno",
                     "Antojitos mexicanos",
                     "72 Virgenes",
                     "Poner un huevo",
                     "Vicente Fox",
                     ])

#Definimos nuestra función para sustituir las palabras
#sustituimos la frase que nos trae de forma global para no causar conflicto a la hora de editarla
#Contamos los espacios en blanco que contiene la frase
#Vamos sustituyendo palabras en los espacios en blanco de forma aleatoria
#Al final imprimimos la frase con las palabras aleatorias agregadas
def sustituir_palabras(String):
    my_string_s = my_string
    blanks = my_string_s.count("_____")
    for i in range(blanks):
        if "_____" in my_string_s:
            my_string_s = my_string_s.replace("_____", np.random.choice(palabras),1)
    print(my_string_s)


#Generamos el metodo constructor inicial para poder correr el programa

if __name__ == '__main__':
    my_string = np.random.choice(frases)
    sustituir_palabras(my_string)
