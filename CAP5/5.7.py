# :: Escreva uma função recursiva chamada contagemRegressiva que aceite um número inteiro como entrada e imprima todos os números de n até 0, seguidos por "Contagem regressiva finalizada!". Por exemplo, a chamada contagemRegressiva(5) deve imprimir 5, 4, 3, 2, 1, 0, "Contagem regressiva finalizada!".


def contagemRegressiva(n): 
    if n == 0: 
        print(n)  
    else: 
        print(n) 
        contagemRegressiva(n-1)
 
contagemRegressiva(5)
 