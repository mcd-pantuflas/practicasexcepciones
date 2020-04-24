#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Este codigo captura los errores introducidos y evita que el programa se rompa.
# Colocamos un while True para que el loop solo rompa si se ingresamente correctamente losdatos pedidos por input
# Tratamos de atrapar ZeroDivisionError, ValueError

# Creamos la funcion de la división.


def division(num1, num2):
    return num1 / num2


while True:

    try:
        num1 = int(input("Ingrese el primer número: "))
        while True:
            num2 = int(input("Ingrese el segundo número: "))
            if num2 > 0:
   break    
            else:
                print("No se puede devidir por 0. intentelo otra vez: ")
                       
# Aquí controlamos la division por 0 que es imposible
    except ZeroDivisionError:
        print("No se puede dividir por 0. Inténtolo de nuevo: ")
    except ValueError:
        print("Inténtelo de nuevo: ")
###
    

print(division(num1, num2))








