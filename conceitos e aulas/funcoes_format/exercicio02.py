n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua nota: "))

nota = (n1 + n2) / 2
#Divisão é prioridade com relação à soma, portanto:
#Para que a soma seja feita antes, é necessário que se coloque a some entre parenteses, pois:
#Os () são priorizados nos calculos matemáticos

print("A nota entre {} e {} é o resultado {}".format(n1, n2, nota))

#Os caracteres () têm prioridade de primeiro nível 
#Os caracteres *, /, **, % tem prioridade de segundo nível em calculos matematicos
#Os caracteres +, - têm prioridade em terceiro nível