
print("¡Hola, mundo!")

entero = 10
flotante = 3.14
texto = "Hola, soy un número"


suma = entero + flotante
multiplicacion = entero * flotante


print(f"Suma: {suma}")
print(f"Multiplicación: {multiplicacion}")

nombre = input("¿Cuál es tu nombre? ")
print("¡Hola, " + nombre + "!")


numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(f"El cuadrado de {num} es {num ** 2}")

while True:
    numero = int(input("Introduce un número mayor a 10: "))
    if numero > 10:
        print("¡Gracias! El número es válido.")
        break
    else:
        print("El número debe ser mayor a 10.")


estudiantes = ["Ana", "Luis", "Pedro", "Marta"]
for estudiante in estudiantes:
    print(estudiante)


contacto = {"Juan": "juan@example.com", "Laura": "laura@example.com"}
for nombre, correo in contacto.items():
    print(f"Nombre: {nombre}, Correo: {correo}")


nuevo_estudiante = input("Introduce el nombre de un nuevo estudiante: ")
estudiantes.append(nuevo_estudiante)
print("Estudiantes actualizados:", estudiantes)


nombre_actualizar = input("Introduce el nombre del contacto a actualizar: ")
nuevo_correo = input(f"Introduce el nuevo correo para {nombre_actualizar}: ")
contacto[nombre_actualizar] = nuevo_correo
print("Contactos actualizados:", contacto)


def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero"

print("Seleccione una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

operacion = input("Elige una opción (1/2/3/4): ")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if operacion == "1":
    print(f"Resultado: {suma(num1, num2)}")
elif operacion == "2":
    print(f"Resultado: {resta(num1, num2)}")
elif operacion == "3":
    print(f"Resultado: {multiplicacion(num1, num2)}")
elif operacion == "4":
    print(f"Resultado: {division(num1, num2)}")
else:
    print("Opción no válida")


import random

numero_aleatorio = random.randint(1, 100)

print("¡Adivina el número! Está entre 1 y 100.")

while True:
    intento = int(input("Introduce tu intento: "))
    
    if intento < numero_aleatorio:
        print("¡Es mayor!")
    elif intento > numero_aleatorio:
        print("¡Es menor!")
    else:
        print("¡Felicidades, adivinaste el número!")
        break

