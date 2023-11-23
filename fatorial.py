#Exercício 1
#Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

n = int(input("Digite o valor de n:"))
i = n-1

if n == 0:
    print(1)
else:
    while i > 0:
        fatorial = n*i
        n = fatorial
        i -= 1

    print (n)   

