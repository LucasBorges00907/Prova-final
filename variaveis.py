def main():
    n = obter_numero_positivo("Digite o valor de n: ")
    for i in range(n):
        texto = obter_texto("Digite o nome da próxima variável: ")
        resultado_em_camel_case = converter_de_snake_para_kamel(texto)
        print(resultado_em_camel_case)





    
def meu_uppercase(letra):
    if "a" <= letra <= "z":
        return chr(ord(letra)- ord("a")+ord("A"))
    return letra
    
    

def converter_de_snake_para_kamel(texto):
    palavras = texto.split('_')
    palavra_convertida = palavras[0]
    for palavra in  palavras[1:]:
        palavra_convertida = palavra_convertida + meu_uppercase(palavra[0]) + palavra[1:]
    return palavra_convertida




def obter_numero(label = 'Digite um número: '):
    numero = input(label)
    while not eh_numero(numero) or numero == '':
        print ("Valor inválido!")
        numero = input(label)
    numero = int(numero)
    return numero


def obter_numero_positivo (label = "Digite um número: "):
    numero = input(label)
    while not eh_numero(numero) or numero == '':
        print ("Valor inválido!")
        numero = input(label)
    numero = int(numero)
    if numero > 0:
        return numero
    else:
        print("O número deve ser positivo!")
        return obter_numero_positivo(label)

def eh_numero(numero):
    for caractere in numero:
        if not eh_algarismo(caractere):
            return False
    return True

def eh_algarismo(caractere):
    algarismos = "0123456789"
    for algarismo in algarismos:
        if caractere == algarismo:
            return True
    return False
    

def obter_texto(label = "Digite uma string: "):
    texto = input(label)
    return texto


def mostrar_texto(texto):
    print(texto)

main()