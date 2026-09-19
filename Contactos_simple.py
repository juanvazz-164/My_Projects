#Funciones
import random
import json
confirmacion = ["si", "sí", "claro", "por supuesto", "afirmativo", "sí, por favor"]
mensajes = ["¡Genial! Continuemos.", "¡Perfecto! Sigamos adelante.", "¡Excelente! Vamos a ello.", "¡Maravilloso! Continuemos.", "¡Fantástico! Sigamos adelante."]
bienvenida = ["¡Bienvenido al programa de contactos!", "¡Hola! Gracias por usar nuestro programa de contactos.", "¡Saludos! Esperamos que disfrutes usando nuestro programa de contactos.", "¡Bienvenido! Estamos encantados de tenerte aquí.", "¡Hola! Gracias por elegir nuestro programa de contactos."]

def guardar_contactos(contactos):
    with open("contactos.json", "w") as archivo:
        json.dump(contactos, archivo)

def cargar_contactos():
    try:
        with open("contactos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def listado(contactos):
    print ("LISTADO DE CONTACTOS")
    print ("-----------------------------")
    contactos.sort(key=lambda contacto: contacto["nombre"].lower())
    for i, contacto in enumerate(contactos, 1):
        print (f"{i}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
    print ("-----------------------------")

def agregar_contacto(contactos):
    while True:
        nombre = input("Ingrese el nombre del contacto: ").strip()

        existe = False
        for contacto in contactos:
            if contacto["nombre"].lower() == nombre.lower():
                existe = True
                break

        if existe:
            print(f"El contacto con el nombre {nombre} ya existe. Por favor, ingrese un nombre diferente.")
            continue
        
        telefono = input("Ingrese el número de teléfono: ")
        contacto = {"nombre" : nombre, "telefono" : telefono}
        contactos.append(contacto)
        print(f"Se ha guardado a {nombre} con el número de teléfono {telefono}")
        print (random.choice(mensajes))
        continuar = input("¿Desea agregar otro contacto? (si/no): ").lower().strip()
        if continuar in confirmacion:
            continue
        else:
            print ("Volviendo al menú principal...")
            break

def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos guardados.")
        input("Presione Enter para volver al menú...")
        return

    listado(contactos)

    print ("Volviendo al menú principal...")
    return
    
def buscar_contacto(contactos):
    if not contactos:
        print ("No hay contactos guardados.")
        return

    print ("-----------------------------")
    nombre = input("Ingrese el nombre del contacto que desea buscar: ").strip()

    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            print ("¡Contacto encontrado!")
            print ("Nombre: ", contacto["nombre"], ", Teléfono: ", contacto["telefono"])
            print ("-----------------------------")
            return

    print ("No se encontró un contacto con el nombre", nombre, ".")

def editar_contacto(contactos):
    if not contactos:
        print ("No hay contactos por editar.")
        input("Presione Enter para volver al menú...")
        return
    
    listado(contactos)

    nombre = input("Ingrese el nombre del contacto que desea editar: ").strip()

    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            print ("Se encontró el contacto", nombre, ".")
            while True:
                print ("Elija qué desea editar:")
                print ("1. Nombre")
                print ("2. Teléfono")
                print ("3. Ambos")

                try:
                    opcion = int(input("Ingrese el número de opción: "))
                except ValueError:
                    print ("Por favor, ingrese un número válido.")
                    continue

                if opcion == 1:
                    nuevo_nombre = input ("Ingrese el nuevo nombre: ")
                    contacto["nombre"] = nuevo_nombre
                    print ("Se ha actualizado el nombre a", nuevo_nombre, ".")
                    break
                elif opcion == 2:
                    nuevo_telefono = input ("Ingrese el nuevo número de teléfono: ")
                    contacto["telefono"] = nuevo_telefono
                    print ("Se ha actualizado el número de teléfono a", nuevo_telefono, ".")
                    break
                elif opcion == 3:
                    nuevo_nombre = input ("Ingrese el nuevo nombre: ")
                    nuevo_telefono = input ("Ingrese el nuevo número de teléfono: ")
                    contacto["nombre"] = nuevo_nombre
                    contacto["telefono"] = nuevo_telefono
                    print ("Se ha actualizado el contacto a Nombre:", nuevo_nombre, ", Teléfono:", nuevo_telefono)
                    break
                else:
                    print ("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

def eliminar_contacto(contactos):
    if not contactos:
        print ("No hay contactos por eliminar.")
        input("Presione Enter para volver al menú...")
        return

    listado(contactos)

    nombre = input("Ingrese el nombre del contacto que desea eliminar: ").strip()

    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            contactos.remove(contacto)
            print (f"Se ha eliminado a {nombre} de la lista de contactos.")
            print (random.choice(mensajes))
            print ("Volviendo al menú principal...")
            return
    
    print (f"No se encontró un contacto con el nombre {nombre}.")
    print ("Volviendo al menú principal...")
        
def main():
    contactos = cargar_contactos()
    while True:
        print ("-------------MENÚ------------")
        print ("Estas son las opciones disponibles:")
        print ("1. Agregar contacto")
        print ("2. Mostrar contactos")
        print ("3. Buscar contacto")
        print ("4. Editar contacto")
        print ("5. Eliminar contacto")
        print ("6. Salir")
        print ("-----------------------------")
        try:
            opcion = int(input("Seleccione el número de opción: "))
        except ValueError:
            print ("Por favor, ingrese un número.")
            continue
        if opcion == 1:
            agregar_contacto(contactos)
            guardar_contactos(contactos)
        elif opcion == 2:
            mostrar_contactos(contactos)
        elif opcion == 3:
            buscar_contacto(contactos)
        elif opcion == 4:
            editar_contacto(contactos)
            guardar_contactos(contactos)
        elif opcion == 5:
            eliminar_contacto(contactos)
            guardar_contactos(contactos)
        elif opcion == 6:
            guardar_contactos(contactos)
            print ("Saliendo del programa...")
            exit()
        else:
            print ("Opción no válida.")

#Código
main()


