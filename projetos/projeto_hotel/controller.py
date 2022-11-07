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
    arquivo = open("hotel/hotel.txt", "r") 
    for line in arquivo:
        index +=1
        if clienteFind == ['nome']:
            chave = index
            flag =1
    arquivo.close()
    if flag == 0:
        print("Cliente não encontrado")
    
    else:
        try:
            with open('hotel/hotel.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                
                # pointer for position
                ptr = 1

                # opening in writing mode
                with open('hotel/hotel.txt', 'w') as fw:
                    for line in lines:
                
                        # we want to remove 5th line
                        if ptr != chave:
                            fw.write(line)
                        ptr += 1
            print("Deleted")

        except:
            print("Oops! someting error")