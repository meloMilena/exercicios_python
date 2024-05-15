# Crie um programa que peça ao usuário para digitar o raio de um círculo. Em seguida, o programa deve calcular e mostrar a área e o comprimento do círculo.
pi = 3.1415926535

raio = float(input("Digite o raio do circulo: "))

area_circulo = pi * (raio ** 2)
comprimento_circulo = 2 * pi * raio

print(f"A area do círculo é  {area_circulo:.1f}") 
print(f"O comprimento do círculo é {comprimento_circulo:.1f}")
