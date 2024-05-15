# Crie um programa que peça ao usuário para digitar um CPF e use uma expressão regular para verificar se o CPF está no formato DDD.DDD.DDD-DD, onde D corresponde a um dígito entre 0 e 9.

import re 
 
cpf_digitado = input("Digite um CPF no formato DDD.DDD.DDD-DD: ") 
padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}' 
 
if padrao.match(cpf_digitado):
    print("CPF valido.") 
else: 
    print("CPF invalido.")

