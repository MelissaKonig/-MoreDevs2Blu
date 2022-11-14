from ex01_pessoaFisica import PessoaFisica
from ex01_pessoaJuridica import PessoaJuridica

pessoaFisica = PessoaFisica("bruno",'02667725018',20.00)
pessoaJuridica =PessoaJuridica("starley",'1002121',20000.00)
print(pessoaFisica)


segundaPf = pessoaFisica.segundo_titular = "edu"
print(segundaPf)



print(pessoaJuridica)

segundaPj = pessoaFisica.segundo_titular = "joe"

print(segundaPj)