from ex02_pessoa import Pessoa

pessoa = Pessoa(
input('Digite seu nome: '),
input('Digite seu CPF: '),
input('Digite sua idade: '),
input('Digite sua altura: '))

print(f'Seu nome é {pessoa.get_nome()}, seu CPF é {pessoa.get_cpf()}, sua idade é {pessoa.get_idade()} e sua altura é {pessoa.get_altura()}.')
print(pessoa)


pessoa2 = Pessoa(
input('Digite seu nome: '),
input('Digite seu CPF: '),
input('Digite sua idade: '),
input('Digite sua altura: '))

print(f'Seu nome é {pessoa2.get_nome()}, seu CPF é {pessoa2.get_cpf()}, sua idade é {pessoa2.get_idade()} e sua altura é {pessoa2.get_altura()}.')
print(pessoa2)