print("//////////////////////////////////////////")
print("     /// ***** T R I V I A ***** ///     ")
print("//////////////////////////////////////////")
print(" ")
name = input("ingrese su nombre:")
print(" ")
print(f"Bienvenido {name} a mi trivia sobre computacion")
print("Pondremos a prueba tus conocimientos.")

print("Responde las siguientes pregutnas escribiendo la letra de la alternativa y presionando 'Enter' para envair tu respuesta:\n")

# Pregunta 1
print("1) Quien fue el creado de windows?\n")
print("a) Linus Torvals")
print("b) Bill Gates")
print("c) Mark Zuckerberg")
print("d) Dennis Ritchie\n")

contador = 0

respuesta_1 = input("Ingrese la respuesta correcta: ")

while respuesta_1 not in ("a","b","c","d"):
  respuesta_1 = input("Debes Responder a, b, c, d. Ingresa nuevamente tu respuesta: ")


if respuesta_1=="b":
  print("Respuesta correcta\n")
  contador +=5
else:
  print("Respuesta incorrecta\n")

print("2) Quien es el CEO de SpaceX?\n")
print("a) Linus Torvals")
print("b) Bill Gates")
print("c) Elon Musk")
print("d) Dennis Ritchie\n")
  
respuesta_2 = input("Ingrese la respuesta correcta: ")

while respuesta_2 not in ("a","b","c","d"):
  respuesta_2 = input("Debes Responder a, b, c, d. Ingresa nuevamente tu respuesta: ")

if respuesta_2=="c":
  print("Respuesta correcta\n")
  contador +=5
else:
  print("Respuesta incorrecta\n") 

print("3) Cual de los siguientes no es un Framework?\n")
print("a) Bootstrap")
print("b) Angular")
print("c) Vue3")
print("d) React\n")
  
respuesta_3 = input("Ingrese la respuesta correcta: ")

while respuesta_3 not in ("a","b","c","d"):
  respuesta_3 = input("Debes Responder a, b, c, d. Ingresa nuevamente tu respuesta: ")

if respuesta_3=="d":
  print("Respuesta correcta\n")
  contador +=5
else:
  print("Respuesta incorrecta\n") 

print("4) Cual de ellos es un framework backend?\n")
print("a) Angular")
print("b) Django")
print("c) Sass")
print("d) Meteor\n")
  
respuesta_3 = input("Ingrese la respuesta correcta: ")

while respuesta_3 not in ("a","b","c","d"):
  respuesta_3 = input("Debes Responder a, b, c, d. Ingresa nuevamente tu respuesta: ")

if respuesta_3=="b":
  print("Respuesta correcta\n")
  contador +=5
else:
  print("Respuesta incorrecta\n") 

if contador > 10 and contador <16:
  print(f"Ha finalizado la Trivia, Obtuvo el puntaje de: {contador} puntos!!, Bien!!!")
elif contador > 15 and contador <21:
  print(f"Ha finalizado la Trivia, Obtuvo el puntaje de: {contador} puntos!!, Excelente!!!")
else:
  print(f"Ha finalizado la Trivia, Obtuvo el puntaje de: {contador} puntos!!, Sera para la proxima, siga intentando")
