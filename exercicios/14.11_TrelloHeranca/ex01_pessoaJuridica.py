from ex01_conta import Conta

class PessoaJuridica():
    segundo_titular = ''

    def __init__(self, titular, cnpj, saldoInicial):
        super().__init__('1030', 'Pessoa')
        self.titular = titular
        self.cnpj = cnpj
        self.saldoInicial = saldoInicial
        print('Passando Pelo Construtor da classe pessoa jurídica')
        
    @property
    def segundo_titular(self):
        return self.segundo_titular  
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.segundo_titular = segundo_titular
    
    def __str__(self):
        return f'{self.titular} {self.cnpj} {self.saldoInicial}'