# Exercício 2 - Desafio do vídeo "Repetição com while"
# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui 
# ao menos um dígito com um dígito adjacente igual a ele.
# Caso exista, imprima "sim"; se não existir, imprima "não".

n = int(input("Digite um numero: "))
anterior = n % 10
n = n // 10;
adjascente = False;
count = 0

while n > 0 and not adjascente:
    atual = n % 10
    if atual == anterior:
        adjascente = True
    else:
        count += 1
    anterior = atual
    n = n // 10

if adjascente:
    print("sim")
else:
    print("não")