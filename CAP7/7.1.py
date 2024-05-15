arquivo = input("Digite o nome do arquivo: ") 
with open(arquivo, "r") as file: 
    conteudo = file.read() 
print(conteudo)
 