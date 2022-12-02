from model.pessoaFisica import PessoaFisica

#Crie a  função create_psf recebendo um atributo interno create_psf (conta)
def create_psf(conta):
    contas = open('pessoafisica.txt', 'a') #Crie uma variável contas escrevendo no arquivo pessoafisica.txt
    contas.write(str(conta)+'\n') #Chame essa variável, chamando a função interna do python que escreve .write()
    contas.close() #Escreva a função  interna contas.close() para fechar o arquivo
    
    
#Crie a função read_psf  dentro do bloco da função crie uma variável lista_contas recebendo uma lista vazia.
def read_psf():
    lista_contas = []
    contas = open('pessoafisica.txt', 'r') #Crie uma segunda variável contas abrindo nosso arquivo txt
    
    #Crie um for com uma variável conta percorrendo a variável contas do arquivo pessoafisica.txt
    for conta in contas:
        conta = conta.strip() #Faça novamente a variável do for conta e atribua a função interna do python Que retira os espaços .strip()
        conta__objeto = conta.split(';')#Crie uma variável conta_objeto recebendo a variável conta e utilize a função interna do python que identifica um índice na lista .split()
        print(conta__objeto)
        #Crie um objeto de pessoaFisica e chame cada atributo da nossa classe, inclusive os dados da classe base (Conta) agencia, numero_agencia, titular, cpf e saldo_incial.
        conta = PessoaFisica()
        conta.agencia = conta__objeto[0] #E insira para cada atributo um índice da lista conforme a sequência de criação
        conta.titular = conta__objeto[1]
        conta.cpf = conta__objeto[2]
        conta.saldo_inicial = conta__objeto[3]
        lista_contas.append(conta) #Chame a variável criada inicialmente, lista_contas e recebendo a função interna do python .append()
    contas.close() #Chame a variável contas do arquivo txt e receba a função interna do python para fechar o arquivo txt
    return lista_contas