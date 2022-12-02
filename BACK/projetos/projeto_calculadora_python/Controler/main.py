from controler import *

poli = "="*20

print(f"\n {poli} CALCULADORA {poli} \n")

operacao = input("Digite a operacao desejada (soma, sub, mult, div): ")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if operacao == "soma":
	print(f"O resultado da operação é: {soma(numero1, numero2)}")

elif operacao == "sub":
	print(subtracao(numero1, numero2))

elif operacao == "mult":
	print(multiplicacao(numero1, numero2))

elif operacao == "div":
	print(divisao(numero1, numero2))

print(f"\n {poli} FIM {poli} \n")