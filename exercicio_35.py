r1 = int(input("Reta 1: "))
r2 = int(input("Reta 2: "))
r3 = int(input("Reta 3: "))

modulo = abs(r2 - r3)
soma = r2 + r3

if r1 > modulo and r1 < soma:
	print("Formam um triângulo.")
else:
	print("Não formam um triângulo.")