import random


def jugar():
    usuario = input("Escoge una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n Yo: ").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        print(f"Compu: {computadora}")
        return 'Empate!'

    if gano_el_jugador(usuario, computadora):
        print(f"compu: {computadora}")
        return 'Ganaste!'

    print(f"compu: {computadora}")
    return 'Perdiste'


def gano_el_jugador(jugador, oponente):
    # Retorna True (verdader) si gana el jugador.
    # Piedra gana a tijera (pi > ti).
    # Tijera gana a Papel (ti > pa).
    # Papel gana a Piedra (pa > pi).
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False

    
    



print(jugar())
