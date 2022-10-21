#Com base nas aulas passadas vamos criar uma calculadora utilizando o conceito de estrutura de decisão.
#crie duas variáveis recebendo dados numéricos com casas decimais, a descrição deve ser relacionada com primeira nota e segunda nota!
#crie uma variável para realizar este cálculo, não esqueça de utilizar o conceito de ordem de procedência aritmética.
#crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console.
#utilizando máscara de substituição imprima de forma descritiva a primeira nota, utilize quebra de linha, imprima a segunda nota, utilize a quebra de linha e imprima o resultado.
#usando estrutura de decisão crie uma condição onde o resultado for maior que sete imprima na sua aplicação console que este aluno está acima da média.
#usando estrutura de decisão crie uma condição onde o resultado for entre cinco e sete imprima na sua aplicação console que este aluno pode solicitar recuperação.
#usando estrutura de decisão crie uma condição onde o resultado for entre quatro e cinco imprima na sua aplicação console que este aluno deve procurar o professor
#Usando estrutura de decisão crie uma condição de saída e imprima na sua aplicação console que este aluno infelizmente não atingiu o esperado!

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))

média = (nota01 + nota02) /2

print(" "*20, "Status do Aluno!", " "*20, "\n")

if média > 7:
    print("Você está acima da média")
    
elif média == 7:
    print("Sua nota está na média")
    
elif média >= 5:
    print("Você precisa solicitar recuperação")
    
elif média >= 4:
    print("Você deve conversar com o professor")
    
else:
    print("Você não tingiu a média")