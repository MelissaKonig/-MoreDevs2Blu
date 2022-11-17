from model import Conta

def create(conta):
    #Variavel referência para txt
    contas = open('contas.txt', 'a')
    #Variável de referência de  escrita
    contas.write(str(conta)+'\n')
    #Variavel de referência fechando o arquivo
    contas.close
    
def read():
    #Lista vazia
    lista_contas = []
    #Variavel de referência do arquivo txt
    contas = open('contas.txt', 'r')
    
    #For com variável percorrendo arquivo txt
    for conta in contas:
        conta__objeto = conta.split(';') #conta.split tira os espaços
        conta = conta.strip()
        #Variavel recebendo função internalizada de condição para o índice
        print(conta__objeto) #printa o espaço alocado na memória
        
        conta = Conta
        conta.titular = conta__objeto[0]
        conta.numero = conta__objeto[1]
        conta.saldo = conta__objeto[2]
        lista_contas.append(conta)
    contas.close
    return lista_contas