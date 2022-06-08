salario = int(input("Qual o seu salário? "))

if salario > 1250:
	novo_salario = salario*1.1
	print("Seu novo salário é: {}".format(novo_salario))
if salario <= 1250:
	novo_salario = salario*1.15
	print("Seu novo salário é: {}".format(novo_salario))