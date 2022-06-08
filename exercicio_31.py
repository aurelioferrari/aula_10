distancia = int(input("Qual a distância da viagem em km? "))

if distancia <=200:
	preço_passagem = 0.5*distancia
else:
	preço_passagem = 0.45*distancia

print("O preço da sua passagem é de R${}".format(preço_passagem))