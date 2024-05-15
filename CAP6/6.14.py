alunos = ["Benjamin", "Hugo", "Aquiles"] 
notas = [6.0, 2.7, 9.7]  
lista_tuplas = [(nome, nota) for nome, nota in sorted(zip(alunos, notas), key=lambda x: x[1], reverse=True)]
