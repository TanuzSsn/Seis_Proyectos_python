# Adivina el numero (computadora)
#La computadora tendra que ir encontrando el numero que escogamos, moviendo los limites de dnde busca

import random

#Definimos nuestra lista de frases a usar cuando no equivoquemos


def adivina_numero_cpu(num_sup):
  print(f"La computadora esta buscando un número entre 1 y {num_sup}")
  opcion = 0
  limit_inf = 1
  limit_sup = num_sup
  numero_cpu = random.randint(limit_inf,limit_sup)

  while opcion != 1:
    print(f"El numero es {numero_cpu} ?")
    opcion = int(input("1: Correcto, 2: Muy bajo, 3: Muy alto  :"))
    if opcion == 1:
      print(f"He adivinado! el numero es {numero_cpu}")
    elif opcion == 2:
      limit_inf = numero_cpu
      numero_cpu = random.randint(limit_inf,limit_sup)
    elif opcion == 3: 
      limit_sup = numero_cpu
      numero_cpu = random.randint(limit_inf,limit_sup)
    else:
      print("Error, seleccióna entre 1, 2 y 3  :")


#Generamos el metodo constructor inicial para poder correr el programa

if __name__ == '__main__':
    num_sup = int(input("Define el limite superior del juego (el inferior es 1 por defecto) :  "))
    adivina_numero_cpu(num_sup)
