try: 
    a = int(input("número a: ")) 
    b = int(input("número b: ")) 
    print(f"Resultado: {a / b}") 
except ZeroDivisionError: 
    print("Erro: Divisão por zero.") 
except ValueError: 
    print("Erro: caracterer invalido")
