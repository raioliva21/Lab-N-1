"""
Una entrada contiene varios casos de prueba. El primer ingreso de un caso de prueba contiene tres n ́umeros
enteros N, C y K que indican, respectivamente, el n ́umero de sorteos que ya han pasado (1 <= N <= 1000),
cuantos n ́umeros comprenden una apuesta (1 <= C <= 10) y el valor m ́aximo de los n ́umeros que pueden ser
escogidos en una apuesta (C <= K <= 100). Luego le siguen N nuevas entradas que contienen C n ́umeros
enteros distintos Xi que indica los n ́umeros extra ́ıdos en cada sorteo anterior (1 <= Xi <= K; para1 <=
i <= C)

"""

# funcion que determina los numeros ganadores del total de numeros apostados
def sorteo(apuestas, C):
    #se importa modulo 'random' para determinar pseudoaleatoriamente los numeros ganadores
    import random
    
    #lista 'ganador' determina los numeros sorteados
    ganador = []
    #lista 'loteria'
    loteria = []
    
    #se inicia sentencia for que determina el o los numeros ganadores
    # los numeros seleccionados dependen de 'C' = la cantidad de numeros ingresados por cada apuesta
    for sorteo in range (0, C):
        # se determina el numero de apuesta, que posteriormente se ingresara como indice en lista 'apuestas'
        # como cada elemento de lista 'apuestas' contiene otros 3 elementos, se debe determinar cual de aquellos 3 ultimos -
        # elementos sera sacado como numero ganador.
        num_apuesta = random.randrange(0,len(apuestas))
        # para sacar numero ganador, se tiene valor de variable indice, determianda aleatoriamente.
        indice = random.randrange(0,C)
        loteria = apuestas[num_apuesta]
        num_ganador = loteria[indice]
        ganador.append(num_ganador)
    
    #se imprimen numeros ganadores
    print(ganador)

    return ganador



def registro_apuestas(C,K):

    # se importa libreria random para el registro de valores al escoger matriz hecha por computadora
    import random

    apuestas = []
    numerosxapuesta = []
    # usurario tiene la opcion de ingresar datos manualmente o que computadora haga simulacion de sorteo
    print("Ingrese <0> si desea ingresar numeros sorteados manualmente")
    decision_sorteo = int(input("Ingrese <1> si desea que computadora realice simulacion de sorteo\n"))

    #si datos son ingresados por usuario
    if decision_sorteo == 0:
        #se realiza ciclo hasta que condicion interna determine un 'break'
        while True:
            #se vacia cadena por cada ciclo for cumplido
            numerosxapuesta = []
            # C equivalente a la cantidad de numeros ingresados por apuesta, determina el limite de ciclo
            for numero in range(0,C):
                #registro de valor ingresado en apuesta (cada apuesta contiene 'C' numeros ) = 'dato'
                dato = int(input(f"Ingrese numero {numero} de apuesta de {C} numeros\n"))
                #control de excepcion
                while C > dato or dato > K:
                    print(f"Error, valor ingresado debe ser mayor a {C} y menor a {K}")
                    dato = int(input("Agrege valor nuevamente, esta vez dentro del rango permitido\n"))
                #se añade 'dato' a lista 
                numerosxapuesta.append(dato)
            #vez cumplida sentencia for, se agrega lista 'numerosxapuesta' como elemento de lista 'apuestas'
            apuestas.append(numerosxapuesta)
            # se pregunta a usurario si se sigue agregando apuestas
            decision_sorteo_2 = input("Ingrese 's' si desea seguir agregando apuestas, 'n' si desea realizar sorteo\n")
            decision_sorteo_2 = decision_sorteo_2.lower()
            if decision_sorteo_2 == 's':
                continue
            #si se acaba con apuestas para realizar sorteo
            else:
                break
    
    #si computadora ingresa apuestas
    elif decision_sorteo == 1:
        #se pregunta a usuario la cantidad de apuestas que realizara computadora
        cantidad_apuestas = int(input(f"Ingrese cantidad de apuestas a realizar. (cada apuesta ingresa {C} numeros) \n"))
        #se ingresan valores aleatorios para matriz relativa a apuestas
        for apuesta in range(0, cantidad_apuestas):
            numerosxapuesta = []
            for numero in range(0,C):
                dato = random.randrange(C,K)
                numerosxapuesta.append(dato)
            apuestas.append(numerosxapuesta)

    #control excepcion
    else:
        print("Error, valor ingresado no es valido")
    
    #se muestra los numeros sorteados
    print(f"Numeros ganadores en sorteo acutal: {apuestas}")
    
    #se retorna 'apuestas', lista que contiene todas las apuestas realizadas (de 'C' elementos cada una)
    return apuestas



# funcion que define 'n', 'c' y 'k'
# tambien realiza contro de excepciones
def registro_y_control_excepcion(frase, limite_inf, limite_sup):
    
    while True:
        n = input(f"Ingrese {frase}: ")
        try:
            n = int(n)
        except ValueError:
            print("valor ingresado no coincide con tipo entero")
        if limite_inf <= n and n <= limite_sup:
            break
        else:
            print(f"Error, valor sobrepasa los limites para {frase}")
    
    return n


def main():
    # se pasan cadenas a variables para luego ser ingresadas como parametros en proxima funcion 'registro_y_control_excepcion'
    n = "el numero de sorteos que ya han pasado"
    c = "la cantidad de numeros ingresados por cada apuesta"
    k = "valor maximo del los numeros ingresados en apuesta"

    # se asigna el argumento de la funcion a variables N,C,K que registran lo indicado en las cadenas al comienzo de porgrama
    # 2do y 3er parametro ingresado definen los limites inf y sup del rango de N,C y K
    N = registro_y_control_excepcion(n,1,100)
    C = registro_y_control_excepcion(c,1,10)
    K = registro_y_control_excepcion(k,C,100)

    #print(N, C, K)

    numeros_excluidos = []
    
    while True:
        #se registran apuestas
        apuestas = registro_apuestas(C, K)
        #se determinan los numeros ganadores
        numeros_ganadores = sorteo(apuestas, C)
        #se agregan los numeros ganadores a la lista de numeros excluidos para no ser ingreados en proximo sorteo (objetivo sw)
        numeros_excluidos.append(numeros_ganadores)
        #se imrpime la lista de numeros excluidos
        print(f"Numeros excluidos (sorteados anteriormente) son: {numeros_excluidos}")
        decision = input("¿Desea continuar con programa? s/n\n")
        decision = decision.lower()
        #continua programa
        if decision == 's':
            continue
        #se utiliza 'break' y acaba ciclo while junto con programa
        elif decision == 'n':
            break
        #control excepcion
        else:
            print("Error, se debe ingresar uno de dos caracteres solicitados")
    


if __name__ == "__main__":
    main()

