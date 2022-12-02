from ex01_conta import Conta

class PessoaFisica(Conta):
    __segundoTitular = ''
    
    def __init__(self, titular, cpf, saldoInicial):
        super().__init__('1030', 'Pessoa')
        self.titular = titular
        self.cpf = cpf
        self.saldoInicial = saldoInicial
        print('Passando pelo construtor da classe Pessoa Física')
        
    @property
    def segundo_titular(self):
        return self.segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.segundo_titular = segundo_titular
        
    def __str__(self):
        return f'{super().__str__()} {self.__titular} {self.__cnpj} {self.__saldo}'