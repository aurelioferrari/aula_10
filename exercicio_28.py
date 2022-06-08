import random

numero = random.randint(0, 5)


usuario = int(input("Qual número estou pensando? "))

if usuario == numero:
	print("Você acertou! Parabéns")
else:
	print("Você não acertou. Tente de novo")
	print("O número que eu pensei foi {}".format(numero))
