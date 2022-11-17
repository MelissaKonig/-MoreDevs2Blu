from ex02_pessoaFisica import PessoaFisica
from ex02_pessoaJuridica import PessoaJuridica

pessoaFisica = PessoaFisica("Melx",'00000',500.00)
pessoaJuridica =PessoaJuridica("Vivi",'00000',700.00)
print(pessoaFisica)


segundaPf = pessoaFisica.segundo_titular = "Haiko"
print(segundaPf)



print(pessoaJuridica)

segundaPj = pessoaFisica.segundo_titular = "Everton"

print(segundaPj)