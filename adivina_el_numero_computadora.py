import random


def adivina_el_numero_computadora(x):

    print("===========================")
    print("  Bienvenido(a) al Juego!  ")
    print("===========================")
    print("Selecciona un numero entre 1 y {x} para que la compu intente adivinarlo")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #Generar prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # Prodian ser ambos.limite_inferior, limite_superior
        
        #Obtener respuesta del usuario
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). si es correcta ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    
    print(f"Siii! La computadora adivino el numero correctamente: {prediccion}")


adivina_el_numero_computadora(10)













