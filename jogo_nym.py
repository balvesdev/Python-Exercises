def computador_escolhe_jogada (n, m):
    cpu_tira = 1

    while cpu_tira != m:
        if (n - cpu_tira) % (m+1) == 0:
            return cpu_tira

        else:
            cpu_tira += 1

    return cpu_tira


def usuario_escolhe_jogada (n, m):
    jogadaValida = False

    while not jogadaValida:
        jogador_tira = int(input('Quantas peças deseja tirar? '))
        if jogador_tira > m or jogador_tira < 1:
            print()
            print('Jogada inválida! Tente novamente.')
            print()

        else:
            jogadaValida = True

    return jogador_tira


def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')


def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    vezDoPC = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            cpu_tira = computador_escolhe_jogada (n, m)
            n = n - cpu_tira
            if cpu_tira == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', cpu_tira, 'peças')

            vezDoPC = False
        else:
            jogador_tira = usuario_escolhe_jogada (n, m)
            n = n - jogador_tira
            if jogador_tira == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogador_tira, 'peças')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')

tipoDePartida = int(input('2 - para jogar um campeonato '))

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()