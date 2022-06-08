import random
# introdução ao game

nome = str(input("Digite o seu nome: "))

print("\nOlá, {}!\n".format(nome))
print("O Objetivo do jogo é chegar a 100 pontos.")
print("Se você acertar o número que eu estou pensando,\nvocê ganha 6 vezes o valor da sua aposta.\n")
print("Se você perder os seus pontos, é Game Over.\n")


numero = random.randint(0, 5)

pontos = 50

print("Você tem {} pontos\n".format(pontos))

# aqui começa o jogo

while pontos > 0 and pontos <100:
	aposta = int(input("Quantos pontos você quer apostar? "))

	numero = random.randint(0, 5)

	usuario = int(input("De 0 a 5, em qual número eu estou pensando? "))

	pontos = pontos - aposta

	while pontos < 0:
		print("Você não tem fichas suficientes para fazer essa aposta.")
		pontos = pontos + aposta
		usuario = 6

	if usuario == numero:
		print("Você acertou! Parabéns!")
		bonus = aposta*6
		pontos = pontos + bonus
		print("\nVocê ganhou {} pontos e sua pontuação atual é: {}".format(bonus, pontos))
		if pontos >= 100:
			print("Você ganhou!")
	else:
		print("Você não acertou. Tente de novo.")
		print("\nSua pontuação atual é: {}".format(pontos))
		if pontos <= 0:
			print("Você perdeu.")
	
else:
	print("Game Over. Obrigado por jogar")