class Pessoa:
    def __init__(self, nome, cpf, idade, altura):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__altura = altura
        
    def set__nome(self, nome):
        self.__nome = nome
    def get__nome(self):
        return self.__nome
    
    def set__cpf(self, cpf):
        self.__cpf = cpf
    def get__cpf(self):
        return self.__cpf
    
    def set__idade(self, idade):
        self.__idade = idade
    def get__idade(self):
        return self.__idade
    
    def set__altura(self, altura):
        self.__altura = altura
    def get__altura(self):
        return self.__altura
    
    def __str__(self):
        return f'Nome: {self.get__nome()}\nCPF: {self.get__cpf()}\nIdade: {self.get__idade()}\nAltura: {self.get__altura()}.'