texto = input("Digite uma frase: ")

print("Tem espaços?",texto.isspace())
print("É alfabético?",texto.isalpha())
print("É alfanumérico?", texto.isalnum())
print("É número?",texto.isnumeric())
print("Espaço entre textos?", ' ' in texto)