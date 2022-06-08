n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

lista = [n1, n2, n3]

lista.sort()

print(lista[:])

print("O maior número é {}".format(lista[0]))
print("O menor número é {}".format(lista[2]))