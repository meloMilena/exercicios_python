# Crie um programa que tenha dois conjuntos de 5 números quaisquer e combine-os usando as operações de união, interseção e diferença, apresentando os resultados de cada operação.

conjunto1 = {3, 14, 15, 92, 65}
conjunto2 = {2, 71, 82, 8, 1}

uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)
diferenca = conjunto1.difference(conjunto2)

print(f"União: {uniao}")
print(f"Interseção: {intersecao}")
print(f"Diferença (Conjunto 1 - Conjunto 2): {diferenca}")