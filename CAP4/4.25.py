# Faça um programa que adicione 30 dias à data atual utilizando timedelta. 

import datetime

data_atual = datetime.date.today()

prox_data = datetime.timedelta(days=30)

data_futura = data_atual + prox_data

print(f"Data atual: {data_atual}")
print(f"Data futura: {data_futura}")
