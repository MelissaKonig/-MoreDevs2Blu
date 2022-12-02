from model import Conta
from controller import create, read


def menu():
    
    dados = Conta()

    dados.titular = 'Melissa König'
    dados.numero = 11273
    dados.saldo = 3200
    create(dados)

    lista_contas = read()

    print(lista_contas)

    for c in lista_contas:
        print(c)
        
menu()