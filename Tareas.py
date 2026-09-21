import random
import json
import os

#Variables
bienvenida = ["Bienvenido a la lista de tareas", "Hola, ¿qué tal?", "¡Bienvenido!", "¡Hola!", "¡Bienvenido a tu lista de tareas!", "¡Hola! ¿Listo para organizar tus tareas?", "¡Bienvenido! Vamos a gestionar tus tareas.", "¡Hola! ¿Qué tal tu día?", "¡Bienvenido! ¿Qué tareas tienes pendientes?", "¡Hola! Vamos a mantener tus tareas en orden."]
completado = ["¡Felicidades! Has completado tu tarea.", "¡Buen trabajo! Tarea completada.", "¡Excelente! Has marcado la tarea como completada.", "¡Genial! Has terminado tu tarea.", "¡Bien hecho! Tarea finalizada.", "¡Perfecto! Has completado la tarea con éxito.", "¡Enhorabuena! Tarea completada correctamente.", "¡Fantástico! Has logrado completar tu tarea.", "¡Maravilloso! Tarea finalizada con éxito.", "¡Increíble! Has completado la tarea satisfactoriamente."]
validado = ["Tu tarea se ha validado correctamente.", "¡Buen trabajo! La tarea ha sido validada.", "¡Excelente! Has validado tu tarea con éxito.", "¡Genial! La tarea ha sido marcada como validada.", "¡Bien hecho! Tarea validada correctamente.", "¡Perfecto! Has completado la validación de la tarea.", "¡Enhorabuena! La tarea ha sido validada satisfactoriamente.", "¡Fantástico! Has logrado validar tu tarea.", "¡Maravilloso! Tarea validada con éxito.", "¡Increíble! Has completado la validación de la tarea."]
po = {"alta": 1, "media": 2, "baja": 3}
VERDE = '\033[92m'
AZUL = '\033[94m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
CELESTE = '\033[96m'
MORADO = '\033[95m'
VIOLETA = '\033[35m'
GRIS = '\033[90m'
NEGRITA = '\033[1m'
RESET = '\033[0m'

#Funciones
def guardar(tareas):
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)

def cargar():
    try:
        with open("tareas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def pedir(tareas):
    tarea = input("¿Qué tarea tienes pendiente? ")
    print("Prioridad: Alta, Media, Baja")
    prioridad = input("¿Qué prioridad le pondrías? ").lower().strip()
    conjunto = {"tarea": tarea, "prioridad": prioridad, "estado": "pendiente"}
    tareas.append(conjunto)
    print (f"{VERDE}{NEGRITA}Se ha agregado la tarea: {tarea} con prioridad {prioridad}.{RESET}")
    print (f"{VERDE}{NEGRITA}{random.choice(validado)}{RESET}")
    input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
    return

def listas(tareas):
    print(f"{AZUL}{NEGRITA}────────────────────{RESET}")
    print(f"{AMARILLO}{NEGRITA}Tareas{RESET}")
    tareas.sort(key=lambda tarea: po.get(tarea["prioridad"].lower(), 4))
    for i, tarea in enumerate(tareas, 1):
        print(f"{AZUL}{NEGRITA}────────────────────{RESET}")
        print(f"{i}. [{tarea['estado']}] {tarea['tarea']} - Prioridad: {tarea['prioridad']}")
        print(f"{AZUL}{NEGRITA}────────────────────{RESET}")

def mostrar(tareas):
    if not tareas:
        print(f"{ROJO}{NEGRITA}No hay tareas guardadas.{RESET}")
        input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
        return

    listas(tareas)
    input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")

def editar(tareas):
    if not tareas:
        print(f"{ROJO}{NEGRITA}No hay tareas.{RESET}")
        input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
        return

    listas(tareas)

    t = input("Escriba la tarea que desea editar: ").strip()

    existe = False
    for tarea in tareas:
        if tarea["tarea"].lower() == t.lower():
            existe = True
            break

    if not existe:
        print(f"{ROJO}{NEGRITA}La tarea no se encontró.{RESET}")
        input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
        return

    for tarea in tareas:
        if tarea["tarea"].lower() == t.lower():
            print(f"{VERDE}{NEGRITA}Tarea encontrada.{RESET}")
            while True:
                print("Lo que puede editar:")
                print("1. Tarea")
                print("2. Prioridad")
                print("3. Ambos")
                try:
                    opcion = int(input("Ingrese el número: "))
                except ValueError:
                    print(f"{ROJO}{NEGRITA}Ingrese un número válido.{RESET}")
                    continue

                if opcion == 1:
                    nt = input("Modifique su tarea: ")
                    tarea["tarea"] = nt
                    print(f"{VERDE}{NEGRITA}Se ha editado la tarea.{RESET}")
                    print(f"{VERDE}{NEGRITA}{random.choice(validado)}{RESET}")
                    input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
                    break
                elif opcion == 2:
                    np = input("Prioridad asignada: ").lower()
                    tarea["prioridad"] = np
                    print(f"{VERDE}{NEGRITA}Se actualizó la prioridad.{RESET}")
                    print (f"{VERDE}{NEGRITA}{random.choice(validado)}{RESET}")
                    input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
                    break
                elif opcion == 3:
                    nt = input("Modifique su tarea: ").lower()
                    np = input("Prioridad asignada: ").lower()
                    tarea["tarea"] = nt
                    tarea["prioridad"] = np
                    print(f"{VERDE}{NEGRITA}Se ha modificado la tarea a: {nt}, y su prioridad es: {np}{RESET}")
                    print(f"{VERDE}{NEGRITA}{random.choice(validado)}{RESET}")
                    input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
                    break
                else:
                    print(f"{ROJO}{NEGRITA}Opción no válida, intente otra vez.{RESET}")

def borrar(tareas):
    if not tareas:
        print(f"{ROJO}{NEGRITA}No hay tareas.{RESET}")
        input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
        return

    listas(tareas)

    te = input("Tarea que desea eliminar: ").strip()

    for tarea in tareas:
        if tarea["tarea"].lower() == te.lower():
            tareas.remove(tarea)
            print(f"{ROJO}{NEGRITA}Se eliminó la tarea de {te}.{RESET}")
            print (f"{VERDE}{NEGRITA}{random.choice(validado)}{RESET}")
            input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
            return

    print(f"{ROJO}{NEGRITA}No se encontró la tarea {te}.{RESET}")
    print(f"{AZUL}{NEGRITA}Volviendo al menú{RESET}")
    input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")

def completar(tareas):
    if not tareas:
        print(f"{ROJO}{NEGRITA}No hay tareas.{RESET}")
        input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
        return

    listas(tareas)

    c = input("Escribe la tarea para marcarla como completada: ").strip()

    for tarea in tareas:
        if tarea["tarea"].lower() == c.lower():
            print(f"{VERDE}{NEGRITA}{random.choice(completado)}{RESET}")
            tarea["estado"] = "completada"
            input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
            return

    print(f"{ROJO}{NEGRITA}No se encontró la tarea.{RESET}")
    input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")

def main():
    tareas = cargar()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print (f"{VERDE}{NEGRITA}{random.choice(bienvenida)}{RESET}")
        print(f"{AZUL}{NEGRITA}┌──────────────────┐{RESET}")
        print(f"{AZUL}{NEGRITA}│ {RESET}{AMARILLO}{NEGRITA}TUS HERRAMIENTAS{RESET}{AZUL}{NEGRITA} │{RESET}")
        print(f"{AZUL}{NEGRITA}└──────────────────┘{RESET}")
        print(f"{AMARILLO}{NEGRITA}1. Añadir una tarea:{RESET} Comience el día organizando sus pendientes.{RESET}")
        print(f"{AMARILLO}{NEGRITA}2. Mostrar tareas:{RESET} Revise sus pendientes y manténgase al día.")
        print(f"{AMARILLO}{NEGRITA}3. Validar su tarea:{RESET} Marque sus tareas completadas y mantenga un registro de su progreso.")
        print(f"{AMARILLO}{NEGRITA}4. Ajuste de tarea:{RESET} Modifique sus tareas y prioridades según sea necesario.")
        print(f"{AMARILLO}{NEGRITA}5. Descartar tarea:{RESET} Elimine tareas que ya no son necesarias o fueron validadas.")
        print(f"{AMARILLO}{NEGRITA}6. Reiniciar:{RESET} El programa reinciará todos los datos.")
        print(f"{AMARILLO}{NEGRITA}7. Salir{RESET}")
        print(f"{AZUL}{NEGRITA}────────────────────{RESET}")
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print(f"{ROJO}{NEGRITA}Ingresa un número.{RESET}")
            continue

        if opcion == 1:
            pedir(tareas)
            guardar(tareas)
        elif opcion == 2:
            mostrar(tareas)
        elif opcion == 3:
            completar(tareas)
            guardar(tareas)
        elif opcion == 4:
            editar(tareas)
            guardar(tareas)
        elif opcion == 5:
            borrar(tareas)
            guardar(tareas)
        elif opcion == 6:
            r = input("¿Está seguro que desea reiniciar el programa? Esto eliminará todas las tareas guardadas. Si/No: ").lower()
            if r == "sí" or r == "si":
                print(f"{ROJO}{NEGRITA}Reiniciando programa...{RESET}")
                tareas.clear()
                guardar(tareas)
            else:
                print(f"{VERDE}{NEGRITA}Operación cancelada, tus tareas están seguras.{RESET}")
                input(f"{GRIS}Presione Enter para regresar al menú...{RESET}")
        elif opcion == 7:
            print(f"{VERDE}{NEGRITA}Cerrando programa...{RESET}")
            exit()
        else:
            print(f"{ROJO}{NEGRITA}Opción ni válida.{RESET} Por favor, seleccione una opción del 1 al 7.")

#Codigo
main()