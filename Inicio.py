print ("Soy tu primer archivo")
nombre = input ("¿Cómo te llamas?")
print ("Qué bien", nombre)
while True:
    años = input("¿Cuántos años cursaste en la secundaria?")
    try:
        años = int (años)
        break
    except ValueError:
        print ("Por favor ingresa un número válido")
if años >=5:
    print ("Wow, tanto tiempo en la secundaria", nombre)
else:
    print("Aún te falta mucho por aprender")
edad = int(input ("¿Cuántos años tienes?"))
if edad >=18:
    print ("Tanto has crecido, seguro ya pagas impuestos", nombre)
else:
    print ("Wow, eres una cosita pequeña aún, pero seguro que crecerás mucho más")
print ("Ahora te haré una pregunta")
respuesta = input ("¿Te gusta estar aprendiendo en VS Code?")
opciones = ["si", "sí", "por supuesto", "claro", "mucho"]
if respuesta in opciones:
    print ("Eso es genial de escuchar")
    respuesta=input ("¿Y te animas a ser programador siempre?")
if respuesta in opciones:
    print ("Espero te agrade la experiencia de programar, y que sigas aprendiendo")
else:
    print ("Bueno, al menos lo intentas")
print ("Bien, ahora", nombre, "intentaré predecir tu color favorito")
colorfavorito = input ("¿Cuál es tu color favorito?")
print ("Bua, que buen color, tu color favorito es el", colorfavorito)
colorfavorito = input ("¿Verdad?")
if colorfavorito == "no":
    print ("Bueno, al menos lo intenté pelotudo xddd")
else:
    print("Acerté, jaja")
print("Es hora de despedirnos", nombre)
for i in range(5):
    print ("Adiós", nombre, "nos vemos en otra ocasión")