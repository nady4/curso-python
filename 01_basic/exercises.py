###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

name = input("Enter your name: ")
city = input("Enter your city: ")
print(f"Hello, {name}")
print(f"You live in {city}")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print("a:", type(a))
print("b:", type(b))
print("c:", type(c))
print("d:", type(d))
print("e:", type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

n = "12345"
n = int(n)
n = float(n)
print("n: ", n, type(n))
f = int(3.99)
print("f: ", f, type(f))

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
print(f"Hello, {name}! Me llamo {name} y tengo {age} anos, mido {height} metros.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.14159
print(pi)
pi = round(pi)
print(pi)
pi = pi // 2
print(pi)