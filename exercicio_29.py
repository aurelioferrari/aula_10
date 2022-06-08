velocidade = int(input("Qual a velocidade que você passou no radar? "))

if velocidade > 80:
	multa = (velocidade - 80)*7
	print("Você foi multado e o valor da multa é de R${}".format(multa))