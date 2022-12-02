from ex01_pessoaFisica import PessoaFisica
from ex01_pessoaJuridica import PessoaJuridica

pessoaFisica = PessoaFisica("Melx",'02667725018',20.00)
pessoaJuridica =PessoaJuridica("Vivi",'1002121',20000.00)

print("MENU PESSOA FISICA: \n")
print(pessoaFisica)
segundaPf = pessoaFisica.segundo_titular = "Morphinho"

print("MENU SEGUNDO TITULAR PESSOA FISICA: \n")
print(segundaPf)

print("MENU PESSOA JURIDICA: \n")
print(pessoaJuridica)
segundaPj = pessoaFisica.segundo_titular = "Euzinha"

print("MENU SEGUNDO TITULAR PESSOA JURIDICA: \n")
print(segundaPj)