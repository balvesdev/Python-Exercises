# Exercício 1
# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. 
# Se o número for primo, imprima "primo". 
# Caso contrário, imprima "não primo".

n = int(input("Digite um número inteiro: "))
i = count = 0

while i <= n or count < 2:
    i += 1
    x = n % i
    if x == 0:
        count += 1

if count <= 2:
    print("primo")
else:
    print("não primo")