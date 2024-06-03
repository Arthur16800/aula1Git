import time

# função que possui muitas atribuições
# parece mais um método
def somar():
    n1 = int(input("digite o primeiro numero da adição:"))
    n2 = int(input("digite o segundo número da adiçao:"))
    print(n1 + n2)

somar()

# função exclusiva de soma de dois números 
def somar2(n1, n2):
    soma = n1 + n2
    return soma

print("Somar 2:", somar2(22, 20))

# Terceiro exxemplo de função
def somar3(n1, n2):
    return n1 + n2 

# numero1 = float(input("digite um número: "))
# numero2 = float(input("digite um número: "))

# # chamada de função 
# print(somar3(numero1, numero2))

# chama
print(somar3(n2 = 12, n1 = 5))

 #funçaõ com parametros default 
def somar4(n1 = 0, n2 = 0):
    return n1 + n2

# print(somar4(50, 25))
# print(somar4())

# função com apenas alguns valores 
def somar5(n1, n2 = 0):
    return n1 + n2

print(somar5(50, 25)) #75
# print(somar5()) #Erro
print(somar5(10)) #10
print(somar5(n2 = 51, n1 = 12))

def somar6(n1, n2):
    if n1 == 1:
        return True

print(somar6(1, 3)) #true
print(somar6(13, 3))#none

print(somar6(1, 2) + 10)#mostra 11
print(somar6(2, 2) + 10)#mostra type não suportado

time.sleep(3)