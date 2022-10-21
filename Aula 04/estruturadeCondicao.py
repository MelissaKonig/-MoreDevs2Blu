#estrutura de decisão

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

média = (n1 + n2) /2

print("Sua média{média}")

if média > 7:
    print("Você está acima da média")
    
elif média == 7:
    print("Você atingiu a média")
    
else:
    print("Você não tingiu a média")