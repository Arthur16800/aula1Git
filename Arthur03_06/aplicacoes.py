import time

# Encontrar o maior valor na lista - Exemplo 1

lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = lista[0] #recebeu o numero 17

for i in range(1, len(lista)):
    if lista[i] > maior_numero:
        maior_numero = lista[i]       
print("O maior número é:", maior_numero)
    
# Exemplo2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i
print("Maior valor 2:", maior)

# Exemplo 3
ultima_lista = my_list[:]
mel = ultima_lista[0]
for i in ultima_lista[1:]:
    if i > mel:
        mel = i
print("Maio valô de 3:", mel)

# Encontrar a localização de um determinado elemento dentro de uma listra
frutas = ["abacaxi", "maçã", "pêra", "mamão", "uva", "melancia"]
elemento = [5]
time.sleep(3)