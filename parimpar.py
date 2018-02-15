#coding: utf-8

print("PARES E IMPARES")
num1 = int(input("Escriba un número entero: "))
num2 = int(input("Escriba un número entero mayor o igual que {num1}: "))

if num2 < num1:
    print("¡Le he pedido un número entero mayor o igual que {num1}!")
else:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print("El número {i} es par")
        else:
            print("El número {i} es impar")
