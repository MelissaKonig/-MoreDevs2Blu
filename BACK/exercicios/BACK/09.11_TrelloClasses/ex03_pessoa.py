class Pessoa:
    nome = ''
    cpf = ''
    idade = ''

    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}, Idade: {self.idade}'