# Crie um programa que peça ao usuário para digitar a distância percorrida por um objeto e o tempo gasto no trajeto. Em seguida, o programa deve calcular e mostrar a velocidade média do objeto.

espaco = float(input("Digite o espaço percorrido: "))
tempo  = float(input("Digite o tempo gasto no trajeto: "))

vm = espaco / tempo
 
print(f"A velocidade média é: {vm} km/h")

