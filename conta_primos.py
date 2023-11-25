def primo(x):
    fator = 2

    # EX: Para x = 3 o resto de x por 2 é = 1, porém 2(fator) é menor 1.5 (3/2), então nao entro no while
    while (x % fator != 0) and (fator <= x/2):
        fator = fator + 1
    # o resto de 3 por 2 é 1, então ele retorna True na função
    if (x % fator != 0) or (x == 2):
        return True
    else:
        return False


def n_primos(x):
    i = 2
    count = 0
    fator = 2
    # i é menor ou igual a 3, então entro no laço.
    while (i <= x):
        if (primo(i)):
            count = count + 1
        i = i + 1
    return count


print(n_primos(int(input('Digite um número inteiro >= 2: '))))
