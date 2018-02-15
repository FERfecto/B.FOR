#coding: utf-8

print ("DIVISORES")
num1 = int(input("escriba un numero mayor que cero: "))
if num1 <= 0:
	print "¡le he pedido un numero entero mayor que cero!"
	
else:
	print "los divisores de", num1, "son:"
	for i in range(1, num1 + 1):
		if num1 % i == 0:
			print (i)
