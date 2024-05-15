def exibir_conteudo_arquivo(nome_arquivo): 
    try: 
        with open(nome_arquivo, 'r') as arquivo: 
            conteudo = arquivo.read()
            print(f"Conteúdo do arquivo '{nome_arquivo}':")
            print(conteudo)
    except FileNotFoundError: 
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo '{nome_arquivo}'")
 
exibir_conteudo_arquivo("jujuba.txt")
 