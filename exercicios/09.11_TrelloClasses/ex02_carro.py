class Carro:
    marca = ''
    modelo = ''
    valor = ''
    
    def __str__(self):
        return f'A marca do carro é {self.marca}, o modelo é {self.modelo} e a cor é {self.valor}'