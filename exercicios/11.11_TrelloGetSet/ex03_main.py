from ex03_conta import Conta

conta = Conta(
    input('Digite o nome do titular: '),
    input('Digite o numero da conta: '),
    input('Digite o saldo a conta: '),
    input('Digite o limite da conta: ')
)
print (f'Titular: {conta.titular} Conta: {conta.numero} Saldo: {conta.saldo} Limite: {conta.limite}')
print(conta)


conta2 = Conta(
    input('Digite o nome do titular: '),
    input('Digite o numero da conta: '),
    input('Digite o saldo a conta: '),
    input('Digite o limite da conta: ')
)
print (f'Titular: {conta2.titular} Conta: {conta2.numero} Saldo: {conta2.saldo} Limite: {conta2.limite}')
print(conta2)