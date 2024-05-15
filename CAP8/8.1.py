class Pessoa: 
    def __init__(self, nome, idade): 
        self.nome = nome 
        self.idade = idade 
 
    def mostrar_dados(self): 
        print(f"Nome: {self.nome}, Idade: {self.idade}") 
 

pessoa1 = Pessoa("Marcos", 80) 
pessoa2 = Pessoa("José", 95) 
 

pessoa1.mostrar_dados() 
pessoa2.mostrar_dados()

