# Adivina el numero

#Vamos a utilizar las librerias de Numpy para trabajar con arreglos/listas
# y con random para seleccionar aleatoriamente datos de estos arreglos/listas

import numpy as np
import random

#Definimos nuestra lista de frases a usar cuando no equivoquemos

frases = np.array([
                    "No joven así no, a ver otra: ",
                    "No que estaba facil?: ",
                    "Andelé, nomas que ese no era: ",
                    "Ya te vas a rendir: ",
                  ])

#Definimos nuestra función para sustituir las palabras
#sustituimos la frase que nos trae de forma global para no causar conflicto a la hora de editarla
#Contamos los espacios en blanco que contiene la frase
#Vamos sustituyendo palabras en los espacios en blanco de forma aleatoria
#Al final imprimimos la frase con las palabras aleatorias agregadas

def adivina_el_numero():
  rango = int(input("Selecciona hasta que numero puedo escoger: "))
  numero_generado = int(random.randint(1,rango))
  numero_usuario = int(input("Adivina un numero entre 1 y "+ str(rango)+": "))
  while (numero_usuario != numero_generado):
    numero_usuario = int(input(np.random.choice(frases)))
  print("Has adivinado el número: " + str(numero_generado))


#Generamos el metodo constructor inicial para poder correr el programa

if __name__ == '__main__':
    adivina_el_numero()
