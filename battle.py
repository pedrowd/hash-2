import sys
from collections import Counter
def quem_ganhou(linha):
    linha = linha.strip()
    ranking = Counter(linha)
    for letra, num in sorted(ranking.items(), key=lambda x: x[1], reverse=True):
        print('    ', letra, num)


def checa_arquivo(nome):
    arquivo = open(nome)
    for i, linha in enumerate(arquivo.readlines()):
        print(i)
        quem_ganhou(linha)

if __name__ == "__main__":
        checa_arquivo(sys.argv[1])
