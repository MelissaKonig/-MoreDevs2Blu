class Animal:
    especie = ''
    cor = ''
    raca = ''
    
    def __str__(self):
        return f'A espécie do animal é {self.especie}, a cor é {self.cor} e a raça é {self.raca}.'