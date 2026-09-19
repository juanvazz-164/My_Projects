print ("¡Hola!, bievenido al organizador de tareas de Python")
nombre = input ("¿Cómo te llamas?")
print ("Muy bien, empecemsos", nombre)
tareas = input ("¿Te gustaría que te diga la prioridad de tus tareas?")
if tareas == "no":
    print ("Está bien, vuelve cuando quieras")
    exit()
else:
    print ("Vale, vamos a ello")
prioridad1 = input ("¿Cuál es tu tarea más importante?")
print (prioridad1, "suena bien, ¿pero en qué grado de prioridad la pondrías?")
while True:
    try:
        nivel= int(input ("Del 1 al 10"))
        break
    except ValueError:
        print ("Por favor pon un número)")
if nivel >=5:
    print ("Vaya", prioridad1, "es de gran prioridad, deberías hacerla ahora mismo")
else:
    print ("Bueno, aún tienes tienes tiempo para jugar bloodsairo xdd")
print ("Y dime", nombre)
pregunta = input ("¿Tienes otra tarea que hacer?")
if pregunta == "no":
    print ("Vale, vueleve cuando gustes")
    exit()
else:
    prioridad2 = input ("¿Cúal otra tarea tienes?")
print (prioridad2, "suena bien, ¿pero en qué grado de prioridad la pondrías?")
while True:
    try:
        nivel2= int(input ("Del 1 al 10"))
        break
    except ValueError:
        print ("Por favor pon un número)")
if nivel2 >=5:
    print ("Bueno, ni modo, deberias hacer eso", nombre)
else:
    print ("Qué bien, más tiempo libre")
print ("Ahora", nombre)
respuesta = input ("¿Ya completaste tus tareas pendientes?")
if respuesta ==  "si":
    print ("¡Qué bien!, me alegro por ti, vamos a elimnar tus tareas de la lista")
else:
    print ("Sale, tendrás que seguirle")
tareas = [prioridad1, prioridad2]
for i in tareas:
    print ("Tu tarea de", i, "ha sido eliminada con éxito", nombre)
peticion = input ("¿Quieres agregar otra tarea a la lista?")
if peticion == "no":
    print ("Está bien, vuelve cuando quieras")
    exit()