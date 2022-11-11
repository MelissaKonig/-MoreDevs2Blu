from ex01_conta import Conta

conta = Conta(
input('Digite seu nome: '),
input('Digite o número da conta: '),
input('Digite o saldo da sua conta: '),
input('Digite o limite da sua conta: '))

print(f'Titular: {conta.get_titular()}, Número da conta: {conta.get_numero()}, Saldo da conta: {conta.get_saldo()}, Limite da conta: {conta.get_limite()}.')
print(conta)

conta2 = Conta(
    input('Digite seu nome: '),
    input('Digite o número da conta: '),
    input('Digite o saldo da sua conta: '),
    input('Digite o limite da sua conta: '))

print(f'Titular: {conta2.get_titular()}, Número da conta: {conta2.get_numero()}, Saldo da conta: {conta2.get_saldo()}, Limite da conta: {conta2.get_limite()}.')
print(conta2)