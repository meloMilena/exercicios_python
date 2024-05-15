# Crie um programa que calcule e mostre o fatorial de um número digitado pelo usuário.
numero = int(input("Digite um número (positivo): ")) 
if numero < 0 :
    print("Não existe fatoria de numero negativo :)")
else:
    fatorial = 1 
    for i in range(1, numero + 1): 
        fatorial *= i 
    print(f"O fatorial é {fatorial}")
