def main():

    ler_arquivo()

def ler_arquivo():
    arquivo = open('alegria.txt','r')
    linhas = arquivo.readlines()
    linhas = map(str.strip, linhas)
    for linha in linhas:
        print(linha)

main()