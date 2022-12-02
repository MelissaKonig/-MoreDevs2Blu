#Crie uma variavel recebendo dados. 
#Esta variavel deve reproduzir em uma aplicação console se os dados que foram digitados estão presentes.
#Ex: "Existe caracter alfabético" / "Existe caracter numerico"

idade = int(input("Qual sua idade? "))

if idade < 18:
	  print("Desculpe, não podemos te servir.") #False
   
if idade > 18:
	  print("Seja bem vinda!") #True
   