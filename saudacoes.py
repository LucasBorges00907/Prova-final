import random

def main():
    nome = input('Qual o seu nome? ')

    print(f'\nOlá {nome}, {alegrias()}')

    numero = int(input('\nDigite um número maior que 0 para uma nova frase e negativo ou 0 para encerrar. '))

    while numero > 0:
        print(alegrias())
        numero = int(input('\nDigite um número maior que 0 para uma nova frase e negativo ou 0 para encerrar. '))

    print(f'\nTchau {nome}, {alegrias()}')




def alegrias():
    arquivo = open('alegria.txt','r',encoding='utf-8')
    saudacoes = arquivo.readlines()
    index = random.randint(0, len(saudacoes) - 1)
    return saudacoes[index].strip()


main()