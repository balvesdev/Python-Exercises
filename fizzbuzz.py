
numero = int(input("Digite um número inteiro:"))

resultado1 = numero % 3
resultado2 = numero % 5

if resultado1 == 0 and resultado2 ==0:
    print("FizzBuzz")
else:
    print(numero)