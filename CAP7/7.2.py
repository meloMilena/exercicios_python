arquivo = input("Digite o nome do arquivo a ser lido: ") 
with open(arquivo, "r") as arquivo: 
    lines = arquivo.readlines() 
    num_linhas = len(lines)
print(num_linhas)
