#Crie uma variavel recebendo dados. 
#Esta variavel deve reproduzir em uma aplicação console se os dados que foram digitados estão presentes.
#Ex: "Existe caracter alfabético" / "Existe caracter numerico"

nome  = input("Qual o seu nome? ")

if nome:	# verifica se o usuário digitou algo (booleano)
    print(f"Você digitou {nome}.") 
else:
    print("Você não digitou nada!")