def pega_palavras(texto):
    palavras = texto.split(" ")
    for palavra in palavras:
        yield palavra

frase = "Há também o misterio do impessoal que é o it"

for palavra in pega_palavras(frase):
    print(palavra)
