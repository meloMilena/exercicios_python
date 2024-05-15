# Crie um programa que encontre e mostre o maior e o menor número em uma lista de 10 números digitada pelo usuário.

n = []
for i in range(10):
    numeros = int(input(f"Digite o numero: "))
    n.append(numeros)
    
maior = n[0]
menor = n[0]
for numeros in n: 
    if numeros > maior: 
        maior = numeros 
    if numeros < menor: 
        menor = numeros 
 
print(f"Maior número digitado {maior}") 
print(f"Menor número digitado {menor}")
 