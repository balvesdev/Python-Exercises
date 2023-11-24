def retangulo(i, l):
    return a == 0 or a == altura-1 or l == 0 or l == largura-1

altura = int(input("Digite a altura do retângulo: "))
largura = int(input("Digite a largura do retângulo: "))

a = 0
while a < altura:
    l = 0
    while l < largura:
        if retangulo(a,l):
            print("#"  ,end = "")
        else:
            print(" ",end = "")
        l += 1
    print()
    a += 1
