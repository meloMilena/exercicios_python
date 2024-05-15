# Crie um programa que calcule e mostre a tabuada de um número digitado pelo usuário.

numero = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")