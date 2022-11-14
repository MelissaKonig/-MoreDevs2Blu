from ex02_conta import Conta

class PessoaJuridica:
    def __init__(self, titular, cnpj, saldo):
        super().__init__('1030', 'Pessoa')
        self.__titular = titular
        self.__cnpj = cnpj
        self.__saldo = saldo
        print('Passando pelo construtor da classe PessoaFisica')
        
    @property
    def segundo_titular(self):
        return self.segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.segundo_titular = segundo_titular
        
    def __str__(self):
        return f'{super().__str__()} {self.__titular} {self.__cnpj} {self.__saldo}'