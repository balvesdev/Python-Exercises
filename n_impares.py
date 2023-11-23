#Exercício 2
#Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. 
#Para a saída, siga o formato do exemplo abaixo.


n = int(input("Digite o valor de n:"))
n = n*2

numero = 1
while numero <= n:
    if numero % 2 !=0:
        print(numero)
    numero+=1
        