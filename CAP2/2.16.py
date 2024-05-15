#Crie um programa que pergunte ao usuário seu peso e sua altura e exiba uma mensagem de acordo com seu IMC (índice de massa corporal), conforme as seguintes regras: "Você está abaixo do peso" se o IMC for menor do que 18,5; "Você está com o peso normal" se o IMC estiver entre 18,5 e 24,9; "Você está com sobrepeso" se o IMC estiver entre 25 e 29,9; ou "Você está com obesidade" caso o IMC seja superior a 29,9.
 

peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print("Você está com o peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
