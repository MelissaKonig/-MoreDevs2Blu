#Trabalho Hotel
#Função horário saudação:
#Import Datetime;
#Import Sleep da lib time;
#Mostre na tela "Bom Dia", "Boa tarde" ou "Boa noite" de acordo com o hoário do sistema;
#Função Menu:
#1-Fazer check-In
#2-Relatório Hospedes
#3-Procurar Hospedes
#4-Fazer Check-Out
#5-Fizalizar Atendimento
#Função Check-In:
#Crie uma lista para o cadastro de pessoas: nome, sobrenome e idade.
from controller import cadastro

#FUNÇÃO HORÁRIO SAUDAÇÃO
from doctest import OutputChecker
from re import A
from xmlrpc.client import DateTime
from time import sleep

hora = input("Digite o horário atual no formato (hh:mm) : ")

x = hora.split(':')
h = x[0]
m = x[1]

if (int(h) < 0 or int(h) > 24) or (int(m) < 0 or int(m) > 59):
    print(f'O horário digitado não possui o formato correto.')

else:
    if (int(h) >= 0 and int(h) <= 11):
        print("Bom dia! Seja bem-vindo!")

    if (int(h) >= 12 and int(h) <= 17):
        print("Boa tarde! Seja bem-vindo")

    else:
        print("Boa noite! Seja bem-vindo!")

print('''
        Como podemos ajudar?

        [A] - Fazer Check-In
        [B] - Relatório Hospedes
        [C] - Buscar Hospede
        [D] - Fazer Check-Out
        [E] - Finalizar Atendimento
    ''')

#FUNÇÃO MENU
poli = "="*20
cabecalho = print(f'\n{poli} Hotel Ponei Saltitante {poli}\n')

escolha = str(input('Escolha uma das opções listadas: '))

checkin = "A"
relatorio = "B"
buscar = "C"
checkout = "D"
finalizar = "E"

if escolha == "A":
    cliente = {}
    cliente["nome"] = input(("Digite seu nome: "))
    cliente["sobrenome"] = input(("Digite seu sobrenome: "))
    cliente["idade"] = input(("Digite sua idade: "))
    cadastro(cliente)