# Crie um programa que verifique se uma pessoa pode votar ou não, considerando sua idade e sua nacionalidade, digitadas pelo usuário (se tem 16 anos ou mais e é brasileiro, pode votar).
 

nacionalidade = input("Digite sua nacionalidade: ")
idade = int(input("Digite a sua idade: "))

if (nacionalidade == "brasileiro" or nacionalidade== "brasileira") and idade >= 16:
    print("Você pode votar")
else:
    print("Você não pode votar")