import random


def adivina_el_numero(x):

    print("===========================")
    print("  Bienvenido(a) al Juego!  ")
    print("===========================")
    print("Tu meta es adivinar el numero generado por la computadora.")

    numero_aleatoreo = random.randint(1, x) # Numero aleatorio en tre 1 y x.

    prediccion = 0

    while prediccion != numero_aleatoreo:
        # El usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) # F- string

        if prediccion < numero_aleatoreo:
            print("Intenta otra vez. Este numero es muy pequeno.")
        elif prediccion > numero_aleatoreo:
            print("Intenta otra vez. Este numero es muy grande.")

    print(f"Felicidades! Adivinaste el numero {numero_aleatoreo} correctamente.")


adivina_el_numero(10)
