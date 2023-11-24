clargura = int(input("Digite a largura:"))
caltura = int(input("Digite a altura:"))


a = 1
while a <= caltura:
    l = 1
    while l <= clargura:
        print("#", end = "")
        l += 1
    print()
    a += 1