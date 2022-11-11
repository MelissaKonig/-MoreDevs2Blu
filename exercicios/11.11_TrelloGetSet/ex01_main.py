from ex01_animal import Animal

animal = Animal(
    input('Digite a espécie do seu bichinho: '),
    input('Digite a raça do seu binhinho: '),
    input('Digite o porte do seu bichinho: '),
    input('Digite a cor do seu bichinho: '))

print(f'Espécie: {animal.especie} Raça: {animal.raca} Porte: {animal.porte} Cor: {animal.cor}.')
print(animal)


animal2 = Animal(
    input('Digite a espécie do seu bichinho: '),
    input('Digite a raça do seu binhinho: '),
    input('Digite o porte do seu bichinho: '),
    input('Digite a cor do seu bichinho: '))

print(f'Espécie: {animal2.especie} Raça: {animal2.raca} Porte: {animal2.porte} Cor: {animal2.cor}.')
print(animal2)