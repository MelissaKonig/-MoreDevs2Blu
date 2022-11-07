#Crie novo documento mainSalario 
#Crie variáveis com tipos predefinidos que suportem a inserção de dados com casas decimais 
#representando os 4 últimos salários de uma pessoa.
#crie uma função de impressão de dados para definir o cabeçalho de uma calculadora, 
#utilizando o conceito de polimorfismo e imprima a palavra calculadora no centro da sua aplicação console.
#Utilizando o conceito de máscara de substituição 
#imprima descritivamente cada salário e a soma entre os mesmos imprimindo o resultado final.
#Ex " primeira variável : {} " os dados devem ser apresentados um em cada linha na sua aplicação console, 
#deve ser utilizado os caracteres especiais de quebra de linha e 
#na impressão deve apresentar apenas duas casas após a vírgula imprima no final 
#utilizando a variável de soma para imprimir o resultado final do seu exercício. 
#No documento controller crie uma função para calcular a soma do salario.

from controller import *

a = float(input("Insira seu salário 01: "))
b = float(input("Insira seu salário 02: "))
c = float(input("Insira seu salário 03: "))
d = float(input("Insira seu salário 04: "))

poli = "="*20

print(f"\n {poli} CALCULADORA {poli} \n")

print("Salário 1: R${:.2f}\nSalário 2: R${:.2f}\nSalário 3: R${:.2f}\nSalário 4: R${:.2f}".format(a, b, c, d))

print("O resultado da soma dos salários é: R${:.2f}".format(somaSalario(a, b, c, d)))

print(f"\n {poli} FIM {poli} \n")