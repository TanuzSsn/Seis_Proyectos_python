#Vamos a jugar piedra papel o tijera
#Importamos las librerias de random y numpy para poder seleccionar aleatoriamente de nuestra lista que tendra las opciones

import random
import numpy as np

#Definimos nuestra funcón para jugar trayendo el dato "user_choice" que es nuestra elección
#Definimos un array con las opciones para que la cpu seleccione aleatoriamente
#comparamos la eleccion de la cpu con la nuestra y definimos con if las opciones empate, ganar y perden
#para ganar podemos definir los 3 casos unicos en los que ganamos y así es mas facil.

def jugar_ppt(user_choice):
  user_choices = user_choice
  opciones = np.array(["piedra", "papel", "tijera"])
  cpu_choices = np.random.choice(opciones)
  if user_choices == cpu_choices:
    print("Ha sido un empate")
  elif (
        (user_choices == "piedra" and cpu_choices =="tijeras")
        or
        (user_choices == "papel" and cpu_choices =="piedra")
        or
        (user_choices == "tijera" and cpu_choices =="papel")
        ):
    print("Has Ganado!")
  else:
    print("Has Perdido!")
  print(f"Tú: {user_choices} -- CPU: {cpu_choices}")

#Funcion principal

if __name__== "__main__":
    print("Vamos a jugar piedra, papel o tijera. Estas listo?")
    user_choice = input("Piedra, Papel o Tijera :   ")
    jugar_ppt(user_choice)