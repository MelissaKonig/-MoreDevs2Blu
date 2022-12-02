#usando a biblioteca interna random use o conceito de importação de toda biblioteca.
#crie quatro variáveis recebendo valores, essas variáveis devem ser com tipos predefinidos tipo string.
#crie uma variável recebendo uma lista das 4 variáveis, logo em seguida utilize importação da biblioteca e atribua a função embaralhar(shuffle).
#essa importação irá realizar o embaralhamento dos valores recebidos atribua a lista a esta função.
#crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console.
#utilizando a interpolação exiba em seguida com a função de impressão a ordem definida dos nomes da variável lista.

from random import shuffle

bichano1 = str(input("Digite um animal de estimação: "))
bichano2 = str(input("Digite um animal de estimação: "))
bichano3 = str(input("Digite um animal de estimação: "))
bichano4 = str(input("Digite um animal de estimação: "))

lista = [bichano1, bichano2, bichano3, bichano4]


print(f"Essa é a lista normal: {lista}")
shuffle(lista)
print("Essa é a lista embaralhada: {lista}")

print(lista)