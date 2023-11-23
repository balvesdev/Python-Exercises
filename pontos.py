import math

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
d = int(input("Digite o quarto número: "))

x = (a - c)**2
y = (b- d) **2

z = math.sqrt((x + y))

if z >= 10:
    print("Longe")
else:
    print("Perto")
