import numpy as np
import string
import random

#varibles
lista_de_palabras = np.array([
                              "Abrir",
                              "Perro",
                              "Dinosaurio",
                              "Correr",
                              "Primero",
                              "Antojo",
                              ])

ahorca_visual = {
                  6: "YA",
                  5: "YA MA",
                  4: "YA MA MAS",
                  3: "YA MA MAS TE",
                  2: "YA MA MAS TE CAR",
                  1: "YA MA MAS TE CAR NAL",
                  0: "YA MA MAS TE CAR NAL </3",    
                  }

def ahorcado():
    print(" ----------------------------------- ")
    print("¡Bienvenido(a) al juego del ahorcado!")
    print(" ----------------------------------- ")
    
    palabra = np.random.choice(lista_de_palabras).upper()

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 6

# Obtener respuesta del usuario mientras existan 
# letras pendientes y al jugador le queden vidas.

    while (len(letras_por_adivinar) > 0 and vidas > 0):
        # Letras adivinadas:
        # ' '.join(['a', 'b', 'c']) --> 'a b c'
        print(f"Te Quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        # Estado actual de la palabra que el jugador debe adivinar (por ejemplo:  H - L A)
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(ahorca_visual[vidas]) # mostrar estado del ahorcado.
        print(f"Palabra: {' '.join(palabra_lista)}") # mostrar las letras separadas por un espacio.

        # El usuario escoge una letra nueva
        letra_usuario = input("Escoge una letra: ").upper()

        # Si la letra escogida por el usuario está en el abecedario
        # y no está en el conjunto de letras que ya se han ingresado,
        # se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            # Si la letra está en la palabra, quitar la letra 
            # del conjunto de letras pendientes por adivinar. 
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
             # Si la letra no está en la palabra, quitar una vida.
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        # Si la letra escogida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra, por favor escoge una letra nueva.")
        else:
            print("Esta letra no es valida")
    
    #El juego llega a esta linea cuando se adivinan todas las letras de la palabra o cuando se agotan las vidas del jugador

    if vidas == 0:
        print(ahorca_visual[vidas])
        print(f"\nLa palabra era {palabra}")
    else:
        print(f"\n¡HAS ADIVINADO LA PALABRA! {palabra}")


if "__main__"==__name__:
    ahorcado()