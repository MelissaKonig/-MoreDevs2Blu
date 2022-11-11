from ex02_carro import Carro

carro = Carro(
    input('Digite a marca do carro: '),
    input('Digite o modelo do carro: '),
    input('Digite a cor do carro: '),
    input('Digite a categoria do carro: ')
)
print(f'Marca: {carro.marca} Modelo: {carro.modelo} Cor: {carro.cor} Categoria: {carro.categoria}')
print(carro)

carro2 = Carro(
    input('Digite a marca do carro: '),
    input('Digite o modelo do carro: '),
    input('Digite a cor do carro: '),
    input('Digite a categoria do carro: ')
)
print(f'Marca: {carro2.marca} Modelo: {carro2.modelo} Cor: {carro2.cor} Categoria: {carro2.categoria}')
print(carro2)