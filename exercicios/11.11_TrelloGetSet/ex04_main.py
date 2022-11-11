from ex04_pessoa import Pessoa

pessoa = Pessoa(
    input('Digite seu nome: '),
    input('Digite seu CPF: '),
    input('Digite sua idade: '),
    input('Digite sua altura: ')
)
print (f'Titular: {pessoa.nome} Conta: {pessoa.cpf} Saldo: {pessoa.idade} Limite: {pessoa.altura}')
print(pessoa)


pessoa2 = Pessoa(
    input('Digite seu nome: '),
    input('Digite seu CPF: '),
    input('Digite sua idade: '),
    input('Digite sua altura: ')
)
print (f'Titular: {pessoa2.nome} Conta: {pessoa2.cpf} Saldo: {pessoa2.idade} Limite: {pessoa2.altura}')
print(pessoa2)