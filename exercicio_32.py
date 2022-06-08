from datetime import date

ano = int(input("Qual o ano? "))

if ano == 0:
	ano = date.today().year


bissexto = ano % 4

if bissexto == 0 and ano % 100 != 0 or ano % 400 == 0:
	print("O ano {} é bissexto.".format(ano))
else:
	print("O ano {} não é bissexto.".format(ano))