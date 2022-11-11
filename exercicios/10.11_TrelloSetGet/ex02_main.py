from ex02_pessoa import Pessoa

pessoa = Pessoa(input('Digite seu nome:> '))
int(input('Digite seu CPF:> '))
float(int('Digite sua idade:> '))
float(input('Digite sua altura:> '))

print (f'Seu nome é {pessoa.get__nome()}, seu CPF é {pessoa.get__cpf}, sua idade é {pessoa.get__idade} e sua altura é {pessoa.get__altura}.')
print(pessoa)


pessoa2 = Pessoa()
input('Digite seu nome: ')
input('Digite seu CPF: ')
input('Digite sua idade: ')
input('Digite sua altura: ')

print (f'Seu nome é {pessoa.get__nome()}, seu CPF é {pessoa.get__cpf}, sua idade é {pessoa.get__idade} e sua altura é {pessoa.get__altura}.')
print(pessoa2)