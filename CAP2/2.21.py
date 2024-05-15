# Crie um programa que simule um semáforo de trânsito. Peça ao usuário para inserir a cor atual do semáforo 
# (verde, amarelo ou vermelho) e utilize a estrutura match..case para imprimir uma ação correspondente. 
# Por exemplo,exemplo, se a cor for verde, imprima "Prossiga"; se for amarelo, imprima "Prepare-se para parar"; 
# se for vermelha, imprima "Pare". Inclua um caso geral que imprima "Cor inválida" para qualquer outra entrada.


cor= input("Insira a cor do semáforo (verde, amarelo ou vermelho): ").lower()


match cor:
    case "verde":
        print("Prossiga")
    case "amarelo":
        print("Prepare-se para parar")
    case "vermelho":
        print("Pare")
    case _:
        print("Cor inválida")
