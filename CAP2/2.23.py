# Desenvolva um "Tradutor de Emoções" que peça ao usuário para inserir uma emoção (feliz, triste, nervoso etc.). Utilize a estrutura match..case para imprimir um emoji correspondente a essa emoção. Por exemplo, imprimir :) para feliz, :( para triste etc.

emocao = input("Insira uma emoção (feliz, triste, nervoso, cansado etc.): ").lower()

match emocao:
    case "feliz":
        print(":)")
    case "triste":
        print(":(")
    case "nervoso":
        print("(º__º)")
    case "cansado":
        print("(~ - ~)")
    case "apatico":
        print("   ")
    case _:
        print("Emoção não cadastrada, tente novamente!")
