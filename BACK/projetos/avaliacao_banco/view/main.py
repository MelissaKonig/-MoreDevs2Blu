from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf

def menu():
    
    #Dentro da função menu() crie uma variável com nome de menu recebendo valor 1
    menu = 1
    
    #Crie um while, abrindo parênteses  atribua à variável menu diferente de zero.
    while (menu != 0):
        #Crie um print descritivo solicitando ao usuário para digitar a opção desejada
        print('''
        Como podemos ajudar?

        [1] Pessoa Física
        [2] Pessoa Jurídica
        ''')
        
        # Crie uma variável menu_inicial recebendo um int() e dentro do int um input solicitando ao usuário opção 1 ou opção 2, estas opções devem ser relacionadas à pessoa física e pessoa jurídica
        menu_inicial = int(input('Digite a opção desejada: '))
        
        # Crie um match recendo a variável menu_incial:
        match menu_inicial:
            # Crie um case 1: opção de escolha para pessoafísica.
            case 1:
                print('-'*20, 'Menu Pessoa Física', '-'*20)
                # Dentro do case 1: crie uma variável menu recebendo um int() e dentro do int, um input solicitando ao usuário opção 1 ou opção 2, estas opções devem estar relacionadas a criar conta de pessoaFísica ou listar conta
                print('''
                Como podemos ajudar?
                
                [1] Cadastrar Pessoa Física
                [2] Listar Pessoas Físicas Cadastradas
                ''')
                
                menu = int(input('Digite a opção desejada: '))
                match menu:
                    # Crie um case 1: opção de escolha para Criar conta pessoaFísica
                    case 1:
                        pessoaFIsica = PessoaFisica() # Dentro do case 1: crie uma variável de referência ao objeto de PessoaFisica()
                        pessoaFIsica.titular = 'Haiko Triste'
                        pessoaFIsica.cpf = '07561592965'
                        pessoaFIsica.saldo_inicial = '52647'
                    
                        print('''
                        Gostaria de cadastrar um segundo titular?
                
                        [1] Sim
                        [2] Não
                        ''')
                        resposta = int(input('Digite a opção desejada: '))
                        
                        # Crie um if condicional solicitando se deseja cadastrar um segundo_titular.
                        if resposta == 1:
                            pessoaFIsica.segundo_titular = input('Digite o segundo titular:> ')
                        
                        
                        #Chame a função create_psf() e passe a variável de objeto
                        create_psf(pessoaFIsica)
                        
                    #Crie um case 2: opção de escolha para listar contas pessoaFísica  
                    case 2:
                        read_psf()
                        
            # Crie um case 2: opção de escolha para pessoajuridica
            case 2:
                # Dentro do case 2: crie uma variável menu recebendo um int() e dentro do int, um input solicitando ao usuário, opção 1 ou opção 2, estas opções devem estar relacionadas a criar conta de pessoaJuridica ou listar conta .
                print('-'*20, 'Menu Pessoa Jurídica', '-'*20)
                print('''
                Como podemos ajudar?
                
                [1] Cadastrar Pessoa Jurídica
                [2] Listar Pessoas Jurídica Cadastradas
                ''')
                
                menu = int(input('Digite a opção desejada: '))
                match menu:
                    #Crie um case 1: opção de escolha para Criar conta pessoaJuridica
                    case 1:
                        #Dentro do case 1: crie uma variável de referência ao objeto de PessoaJuridica()
                        conta = PessoaJuridica() #Chame cada atributos da nossa classe através da variável de referência do objeto e insira input solicitando dados para o cadastro.
                        conta.titular = 'Melissa Konig'
                        conta.cnpj = '25600001450001'
                        conta.saldo_inicial = '50690'
                        
                        print('''
                        Gostaria de cadastrar um segundo titular?
                
                        [1] Sim
                        [2] Não
                        ''')
                        resposta = int(input('Digite a opção desejada: '))
                        
                        #Crie um if condicional solicitando se deseja cadastrar um segundo_titular.
                        if resposta == 1:
                            conta.segundo_titular = 'Não Possui'
                            
                        #Chame a função create_pj() e passe a variável de objeto
                        create_pj(conta)
                        
                    # Crie um case 2: opção de escolha para listar conta pessoaJuridica
                    case 2:
                        # Dentro do case 2: chame a função read_pj() para listar
                        listar_pj = read_pj()
                        for c in listar_pj:
                            print(c)