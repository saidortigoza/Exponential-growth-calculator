'''
Pensamiento computacional para Ingeniería
TC 1028.8

Said Guadalupe Ortigoza Trujillo, A01707430

Explicación del funcionamiento del programa:
Este proyecto calcula la razón de crecimiento exponencial del país que desee el usuario
en un lapso de tiempo establecido por el usuario en años, y despliega un menú de opciones entre las
que el usuario puede elegir, por ejemplo: desplegar la gráfica del crecimiento poblacional o
imprimir la población en un año ingresado por el usuario.
Se le pedirá al usuario la población inicial y final en un lapso de tiempo. El programa calculará la
razón de crecimiento “r” utilizando la fórmula r = 1/t * ln (P/Pi) y la utilizará para
calcular la población esperada en el año siguiente.

'''

#La librería matplotlib se utiliza para mostrar la gráfica
import matplotlib.pyplot as plt

#La librería math se usa para utilizar la función exponencial
import math

#Arreglos del programa
poblacion = []
años = []

#Funciones secundarias:
#La función arreglo_años crea un arreglo para guardar desde el año inicial hasta el final + 1
def arreglo_años(rango,yeari,años):
    for i in range(rango+2):
        años.append(yeari)
        yeari += 1
    return años

#La función arreglo_poblacion almacena la población para cada año
def arreglo_poblacion(rango,poblacion,razon,pi):
    for i in range(rango+2):
        psiguiente = round(pi*math.e**(razon*(i)))
        poblacion.append(psiguiente)
    return poblacion

#Función menú del programa
def menu():
    print("\n1. Imprime razón de cambio")
    print("2. Muestra población")
    print("3. Imprime gráfica")
    print("4. Salir")

#La función imprime_gráfica asigna la población al eje y y los años al eje x para desplegar una gráfica
def imprime_grafica(poblacion,mapeado,años):
    plt.plot(poblacion)
    plt.xticks(mapeado, años)
    plt.title('Crecimiento poblacional')
    plt.xlabel('Años')
    plt.ylabel('Población')
    plt.show()
    
#Función principal
def main():
    print("Bienvenido. Este programa calcula el crecimiento poblacional del país que desee ingresar.")
    nombre = input("\nPor favor ingrese el nombre del país: ")

    print("\nA continuación ingrese el lapso de tiempo a analizar.")

    yeari = int(input("\n¿Cuál es el año inicial? "))
    yearf = int(input("\n¿Cuál es el año final? "))
    rango = yearf - yeari

    pi = int(input("\n¿Cuál era su poblacion el primer año? "))
    pf = int(input("\n¿Cuál es su población en el año final? "))
    
    razon = round((1/rango)*math.log(pf/pi),5)
    
    arreglo_años(rango,yeari,años)
    arreglo_poblacion(rango,poblacion,razon,pi)
    mapeado = range(len(años))
    
    continua = True
    
    while continua:
        
        menu()
        opcion = int(input("\n¿Qué acción desea realizar? "))
        
        if opcion == 1:
            print("\nLa razón de cambio de",nombre,"es",razon)
        elif opcion == 2:
            print("\nEl año que ingreses debe estar dentro del rango que ingresaste o ser el año siguiente al último.")
            a = int(input("¿En qué año desea ver la población? "))
            for i in range(len(años)):
                if años[i] == a:
                    print("\nLa población en el año",a,"es aproximadamente",poblacion[i],"habitantes.")
        elif opcion == 3:
            imprime_grafica(poblacion,mapeado,años)
        elif opcion == 4:
            print("\nGracias por usar el programa. Vuelva pronto.")
            continua = False
        else:
            print("\nLo siento. La opción que ingresaste no es válida.")
            continua = False

main()
