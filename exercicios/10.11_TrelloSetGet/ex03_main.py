from ex03_carro import Carro

carro = Carro(
input('Digite a marca do carro: '),
input('Digite o modelo: '),
input('Digite a cor: '),
input('Digite a categoria: '))

print(f'Marca {carro.get_marca()}, Modelo: {carro.get_modelo()}, Cor: {carro.get_cor()}, Categoria: {carro.get_categoria()}.')
print(carro)


carro2 = Carro(
input('Digite a marca do carro: '),
input('Digite o modelo: '),
input('Digite a cor: '),
input('Digite a categoria: '))

print(f'Marca {carro2.get_marca()}, Modelo: {carro2.get_modelo()}, Cor: {carro2.get_cor()}, Categoria: {carro2.get_categoria()}.')
print(carro2)