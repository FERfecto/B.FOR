#coding: utf-8

num1 = int(input("cuantos valores va a introducir?: "))
if num1 < 1:
	print ("Imposible!")
else:
	num2 = int(input("escriba un numero: "))
	for i in range(num1 - 1):
		num3 = int(input("escriba un numero mayor que" + str(num2) + ": "))
		if num3 <= num2:
			print (num3, "no es mayor que", num2)
		
