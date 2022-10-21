#com base nas aulas passadas vamos criar um sorteio de lista e utilizando o conceito de estrutura de decisão exibir qual foi a posição de ordem de inserção de dados que foi sorteada.
#usando o conceito de importação otimizada importe a função choice,
#logo em seguida crie quatro variáveis representadas por nomes n1, n2, n3, n4, essas variáveis devem ser do tipo string e devem solicitar dados. 
#crie uma variável que receba como lista estas quatro variáveis.
#crie uma variável usando a importação otimizada e atribuindo a variável lista. 
#crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console.
#utilizando o conceito de interpolação exiba qual foi o nome sorteado.
#utilizando o conceito de estrutura de decisão cria uma condição que exiba a ordem em que foi digitado o nome sorteado pela variável de sorteio da lista!

import random

n1 = str(input("Digite um número: "))
n2 = str(input("Digite um número: "))
n3 = str(input("Digite um número: "))
n4 = str(input("Digite um número: "))

lista = [n1, n2, n3, n4]

sorteado = random.choice(lista)

print(" "*20, "Sorteio aleatorio.com", " "*20, "\n")

print("O número Sorteado foi {}! ".format(sorteado))

if sorteado == n1: 
    print("O número sorteado foi o primeiro")
    
if sorteado == n2: 
    print("O número sorteado foi o segundo")
    
if sorteado == n3: 
    print("O número sorteado foi o terceiro")
    
if sorteado == n4: 
    print("O número sorteado foi o quarto")