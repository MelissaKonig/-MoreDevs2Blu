from model.pessoaJuridica import PessoaJuridica

#Crie a  função create_pj recebendo um atributo interno create_pj (conta)
def create_pj(conta):
    contas = open('pessoajuridica.txt', 'a') #Crie uma variável contas escrevendo no arquivo pessoajuridica.txt
    contas.write(str(conta)+'\n') #Chame essa variável, chamando a função interna do python que escreve .write()
    contas.close() #Escreva a função  interna contas.close() para fechar o arquivo
    
#Crie a função read_pj()  dentro do bloco da função crie uma variável lista_contas recebendo uma lista vazia.
def read_pj(conta):
    lista_contas = []
    contas = open('pessoajuridica.txt', 'r') #Crie uma segunda variável contas abrindo nosso arquivo txt
    
    for conta in contas:
        conta__objeto = conta.split(';')
        conta = conta.strip()
        print(conta__objeto)
        
        conta = PessoaJuridica()
        conta.agencia = conta__objeto[0] #Crie uma variável conta_objeto recebendo a variável conta e utilize a função interna do python que identifica um índice na lista .split()
        conta.titular = conta__objeto[1] #Crie um objeto de pessoaJjuridica e chame cada atributo da nossa classe, inclusive os dados da classe base (Conta) agencia, numero_agencia, titular, cnpj e saldo_inicial.
        conta.cnpj = conta__objeto[2]
        conta.saldo_inicial = conta__objeto[3]
        lista_contas.append(conta) #Chame a variável criada inicialmente, lista_contas e recebendo a função interna do python .append()
    contas.close() #Chame a variável contas do arquivo txt e receba a função interna do python para fechar o arquivo txt
    return lista_contas