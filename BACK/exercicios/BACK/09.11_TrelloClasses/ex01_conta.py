class Conta:
    numero = 0
    titular = ''
    saldo = 0
    limite = 0
    
    def __str__(self): #def = define (metodo único de python)
        return f'O número da conta é {self.numero}, o titular é {self.titular}, o saldo é {self.saldo} e o limite é {self.limite}'