
import random

def eleccion_numeros(matriz, total_apuestas):

    jugadores = []
    numeros = []
    matriz = [jugadores, numeros]
    i = -1

    #se ingresa a ciclo infinito while
    while True:
        #se solicita ingresar nombre de jugador
        jugador = input("Ingrese nombre de apostador: ")
        #se agrega nombre a lista 'jugadores'
        jugadores.append(jugador)
        # se ingresa un numero en condicional while
        i+= 1
        while True:
            numero = input(int("Ingrese numero"))
            #se evalua validez de dato ingresado
            while numero in matriz[i, numeros]:
                try:
                    numero = int(numero)
                except TypeError:
                    print("El tipo de dato ingresado es invalido")
                if numero in matriz[i, numeros]:
                    print(f"Error. Numero {numero} ha sido ingresado mas de una vez")
                else:
                    break
            numeros.append(numero)
            total_apuestas += 1
            continuar_apuesta_jugador = input("¿Desea continuar con apuesta? s/n")
            continuar_apuesta_jugador = continuar_apuesta_jugador.lower()
            if continuar_apuesta_jugador == 'n':
                break
        print("marque 's' para continuar apuestas con el siguiente jugador")
        continuar_apuestas = input("marque 'n' para acabar con las apuestas y realizar sorteo de numeros")
        continuar_apuestas = continuar_apuestas.lower()
        if continuar_apuestas == 'n':
            break
        else:
            numeros = []


    
def sorteo_numeros(matriz, total_apuestas):

    numeros_sorteados = total_apuestas / 10
    numeros_ganadores = []
    #se realiza sorteo pseudoaletario
    print("Los numeros ganadores son:", end=' ')
    for i in range (0,numeros_sorteados):
        numeros_ganadores[i] = matriz(random.randint(1, 100))
        print(f"{numeros_ganadores[i]}", end=" ")

def main():
    
    total_apuestas = 0
    matriz = []
    eleccion_numeros(matriz, total_apuestas)
    sorteo_numeros(matriz, total_apuestas)

if 0 == 0:
    main()


