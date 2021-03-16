import battle
import draw

def jogar():
    tabuleiro = {}
    for x in draw.LINHAS:
        for y in draw.COLUNAS:
            tabuleiro[x + str(y)] = None
    draw.vazio()
    p1 = input("Escolha o símbolo do jogador 1:\n")
    p2 = input("Escolha o símbolo do jogador 2:\n")
    ganhou = False
    while not ganhou:
        p1_ok = False
        p2_ok = False
        while not p1_ok:
            p1_move = input("Digite a letra e número para jogador 1:\n")
            if p1_move not in tabuleiro:
                print("Letra e número não estão no tabuleiro:", p1_move)
                continue
            if tabuleiro[p1_move] == None or tabuleiro[p1_move] == p2:
                p1_ok = True
            else:
                print("Posição inválida para jogador 1", p1_move, tabuleiro[p1_move])
        while not p2_ok:
            p2_move = input("Digite a letra e número para jogador 2:\n")
            if p2_move not in tabuleiro:
                print("Letra e número não estão no tabuleiro:", p2_move)
                continue
            if tabuleiro[p2_move] == None or tabuleiro[p2_move] == p1:
                p2_ok = True
            else:
                print("Posição inválida para jogador 2", p2_move, tabuleiro[p2_move])
        if tabuleiro[p1_move] == None:
            tabuleiro[p1_move] = p1
            print(p1_move, "=", tabuleiro[p1_move])
        elif tabuleiro[p1_move] == p2:
            x = input("Batalha!")
            print(x)
            battle.quem_ganhou(x)
        p2_move = input("Digite a letra e número para jogador 2:\n")

jogar()
