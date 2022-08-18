import random
import string

from  palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    # Seleccionar una palabra al azar de la lista, de palabras validas.
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()
    

def ahorcado():

    print("===========================")
    print("  Bienvenido(a) al Juego!  ")
    print("===========================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letra_adivinadas = set()
    abecedario =  set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letra_adivinadas)}")

        # Mostrar el estado actual de la palabra
        # H - L A
        palabra_lista = [letra if letra in letra_adivinadas else "-" for letra in palabra] # Esta sintaxis se llama  List Comprehension
        # Mostrar las estado del ahorcado.
        print(vidas_diccionario_visual[vidas])
        # Mostrar las letras separadas por un espacio.
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        '''
        Si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras que ya se han ingresado, se anade la letra al conjunto
        de letras ingresadas.
        ''' 
        if letra_usuario in abecedario - letra_adivinadas:
            letra_adivinadas.add(letra_usuario)

            # Si la letra esta en la palabra
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra.")
        
        elif letra_usuario in letra_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es valida.")

    #El juego llega a esta linea cuando se adivinan todas las letras de la palabra o cuando se agotan las vidas del jugador.

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f"Excelente! Adivinaste la palabra {palabra}!")
    input("Enter para salir")


ahorcado()