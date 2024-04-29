a = 5
b = 10
print ("Hola mundo")
print ("La suma es: ", a+b)
print ("La resta es: ", a-b)
print ("****************************")
print ("*********CALCULADORA*************")
print ("****************************")
c=int(input("insertar el primer dato: "))
d=int(input("insertar el segundo dato: "))

print("La suma de los datos es: ", c+d)
print("La resta de los datos es: ", c-d)
print("La multiplicacion de los datos es: ", c*d)
print("La division de los datos es: ", c/d)
print("Gracias")



def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No es posible dividir entre 0"


operacion = input("¿Qué operación quieres realizar? (+, -, *, /): ")


numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))


if operacion == '+':
    print("El resultado es:", sumar(numero1, numero2))
elif operacion == '-':
    print("El resultado es:", restar(numero1, numero2))
elif operacion == '*':
    print("El resultado es:", multiplicar(numero1, numero2))
elif operacion == '/':
    print("El resultado es:", dividir(numero1, numero2))
else:
    print("Operación no válida")
