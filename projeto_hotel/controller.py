#  ! FUNÇÃO SALVAR CADASTRO HOSPEDES !
def cadastro(cliente):
    with open('nomes.txt','a') as arquivo:
        arquivo.write(str(cliente)+"\n")

#  ! FUNÇÃO LISTAR HOSPEDES CADASTRADOS !
def listar():
    with open('nomes.txt','r') as arquivo:
        print(arquivo.read())

#  ! FUNÇÃO BUSCAR HOSPEDE !
def clienteFind():
    with open('nomes.txt','r') as arquivo:
        print(arquivo.get())

#  ! FUNÇÃO DELETAR HOSPEDE !
def fazerCheckout(clienteFind):
    
    index=0
    flag=0
    arquivo = open('nomes.txt', 'r')
        
    for line in arquivo:
        index +=1
        if clienteFind == eva1(line)['nome']:
            chave = index
            flag =1
    if flag == 0:
        print("Cliente não encontrado")
    arquivo.close()