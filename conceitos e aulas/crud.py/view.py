from model import Conta
from controller import read
from controller import create

abacate = Conta()
abacate.titular = 'Jean Carlos Niuhs'
abacate.numero = '12345'
abacate.saldo = 30000.0

create(abacate)

lista_abacates = read()

print(lista_abacates)

print('*'*30)

for c in lista_abacates:
    print(c)