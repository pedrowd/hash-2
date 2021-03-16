LINHAS = list("ABCDE")
COLUNAS = range(1, 6)
SEPARA_LINHA = "+--+--+--+--+--+"
SEPARA_COLUNA = "|"

def vazio():
    print(" " * 5 + "  ".join(str(col) for col in COLUNAS))
    print(" " * 4 + SEPARA_LINHA)
    for lin in LINHAS:
        print(lin + " " * 3 + "  ".join(list(SEPARA_COLUNA * 6)))
        print(" " * 4 + SEPARA_LINHA)

if __name__ == "__main__":
    vazio()

