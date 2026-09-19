#Funciones
def menu():
    modos = ("suma", "resta", "multiplicación", "división")
    print ("Bien, estos son los modos que te puedo ofrecer: ", modos)
    while True:
            print ("¿Con cuál quieres empezar?")
            ayuda = input ("Escoge entre suma, resta, multiplicación o división " ).lower().strip()
            if ayuda == "suma":
                print ("Has escogido sumar")
                resultado = suma()
                print ("El resultado es:", resultado)
                break
            elif ayuda == "resta":
                print ("Has escogido restar")
                resultado = resta()
                print ("El resultado es:", resultado)
                break
            elif ayuda == "multiplicación":
                print ("Has escogido multiplicar")
                resultado = multiplicacion()
                print ("El resultado es:", resultado)
                break
            elif ayuda == "división":
                print ("Has escogido dividir")
                resultado = division()
                print ("El resultado es:", resultado)
                break
            else:
                print ("Por favor elige uno de los modos proporcionados ")
                continue

def suma():
    n1 = float(input("Ingresa un número "))
    n2 = float(input("Ingresa otro número "))
    resultado = n1 + n2
    return resultado

def resta():
    n1 = float(input("Ingresa un número "))
    n2 = float(input("Ingresa otro número "))
    resultado = n1 - n2
    return resultado

def multiplicacion():
    n1 = float(input("Ingresa un número "))
    n2 = float(input("Ingresa otro número "))
    resultado = n1 * n2
    return resultado

def division():
    n1 = float(input("Ingresa un número "))
    n2 = float(input("Ingresa otro número "))
    while n2 == 0:
        print ("No se puede dividir entre 0")
        n2 = float(input("Por favor ingresa otro número diferente a 0 "))
    resultado = n1/n2
    return resultado

def continua(confirmacion, nombre):
    continuar = input("¿Deseas continuar? ").lower().strip()
    if continuar in confirmacion:
        menu()
    else:
        print ("Vale", nombre, "está bien")
        exit()


#Inicio del programa
print ("Hey, qué tal, soy Frager, tu chatbot personal")
nombre = input ("¿Cómo te llamas? ")
print (nombre, "es buen nombre, me alegro, y bien...")
ayuda = input ("¿Necesitas algo de ayuda? ").lower().strip()
confirmacion = ["si", "sí", "por supuesto", "sip", "claro", "chi", "chipi"]
if ayuda in confirmacion:
    print ("Muy bien, te puedo brindar algunos modos que tengo disponibles para ti")
else:
    print ("Está bien, estaré aquí cuando lo requieras, ¡suerte!", nombre)
    exit ()
menu()
continua(confirmacion, nombre)


    