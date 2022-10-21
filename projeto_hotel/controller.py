def cadastro(cliente):
    with open("nomes.txt","a") as arquivo:
        arquivo.write(str(cliente)+"\n")

def listar():
    nomes = []
    with open("nomes.txt","r") as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)

    return nomes