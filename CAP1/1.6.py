# Crie um programa que peça ao usuário para digitar um número. Em seguida, o programa deve calcular e mostrar a raiz quadrada desse número.

import math

numero = int(input("Digite o número:"))

sqrt_num = math.sqrt(numero)

print(f"A raiz quadrada de {numero} é {sqrt_num:.1f}")