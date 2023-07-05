def main():
    mostrar_texto (f"As figuras disponíveis são : Quadrado,Retângulo,Triângulo,Trapézio e círculo")
    primeira_figura = obter_texto("Digite a letra inicial da 1° figura (Digite P para trapézio): ")
    while primeira_figura != 'Q' and primeira_figura != 'q' and primeira_figura !='R' and primeira_figura != 'r' and primeira_figura != 'T' and primeira_figura != 't' and primeira_figura != 'P' and primeira_figura !='p' and primeira_figura != 'C' and primeira_figura != "C":
        mostrar_texto("Figura inválida! Digite uma letra válida!")
        primeira_figura = obter_texto("Digite a letra inicial da 1° figura (Digite P para trapézio): ")

    segunda_figura = obter_texto("Digite a letra inicial da 2° figura (Digite P para trapézio): ")

    while primeira_figura == segunda_figura: 
        mostrar_texto("As duas figuras não podem ser do mesmo tipo! Digite novamente!")
        segunda_figura = obter_texto("Digite novamente, a letra inicial da 2° figura (Digite P para trapézio): ")


    while segunda_figura != 'Q' and segunda_figura != 'q' and segunda_figura !='R' and segunda_figura != 'r' and segunda_figura != 'T' and segunda_figura != 't' and segunda_figura != 'P' and segunda_figura !='p' and segunda_figura != 'C' and segunda_figura != "C":
        mostrar_texto("Figura inválida! Digite uma letra válida!")
        segunda_figura = obter_texto("Digite novamente, a letra inicial da 2° figura (Digite P para trapézio): ")

   
    area_figura_1 = calcular_area(primeira_figura)
    area_figura_2 = calcular_area(segunda_figura)

    tipo_figura_1 = verificar_tipo_figura(primeira_figura)
    tipo_figura_2 = verificar_tipo_figura(segunda_figura)

    percentual_entre_areas = calcular_proporcao_percentual_das_areas(area_figura_1,area_figura_2)

    mostrar_texto(f"A figura 1 é um {tipo_figura_1} e sua área é de {area_figura_1:.2f}")
    mostrar_texto(f"A figura 2 é um {tipo_figura_2} e sua área é de {area_figura_2:.2f}")

    if  area_figura_1 == area_figura_2:
        mostrar_texto(f"As figuras tem a mesma área! ")
    elif area_figura_1>area_figura_2:
        mostrar_texto(f"A maior área é a da figura 1")
    else:
        mostrar_texto(f"A maior área é a da figura 2")

    
    mostrar_texto(f"A proporção  percentual entre a área da menor figura sobre a área da maior é de {percentual_entre_areas:.2f}% ")




def calcular_area(figura):
    if figura == 'Q' or figura == 'q':
            lado_quadrado = obter_numero_positivo("Digite o valor do lado de seu quadrado: ")
            area = calcular_area_quadrado(lado_quadrado)

    elif figura == 'R' or figura == 'r':
            comprimento_retangulo =obter_numero_positivo("Digite o valor do comprimento de seu retângulo: ")
            largura_retangulo = obter_numero_positivo("Digite o valor da largura de seu retângulo: ")
            area = calcular_area_retangulo(comprimento_retangulo,largura_retangulo)

    elif figura == 'T' or figura == 't':
            base_triangulo = obter_numero_positivo("Digite a base do triângulo: ")
            altura = obter_numero_positivo("Digite a altura do triângulo: ")
            area = calcular_area_triangulo(base_triangulo,altura)

    elif figura == 'P' or figura == 'p':
            base_menor_trapézio = obter_numero_positivo("Digite a base menor do trapézio: ")
            base_maior_trapézio = obter_numero_positivo("Digite a base maior do trapézio: ")
    
            while base_maior_trapézio <= base_menor_trapézio:
                 mostrar_texto("A base maior, deve OBRIGATORIAMENTE maior que a base menor! ")
                 base_maior_trapézio = obter_numero_positivo("Digite um novo valor para a base menor do trapézio: ")
            altura_trapezio = obter_numero_positivo("Digite a altura do trapézio: ") 
            area = calcular_area_trapezio(base_maior_trapézio,base_menor_trapézio,altura_trapezio)
            
    elif figura == 'C' or figura == 'c':
            pi = 3.14159
            raio = obter_numero_positivo("Digite o raio do círculo: ")
            area = calcular_area_circulo(pi,raio)
    return area



def verificar_tipo_figura(figura):
        if figura == 'Q' or figura == 'q':
            figura = "Quadrado"
            return figura
        elif figura == 'R' or figura == 'r':
            figura = "Retângulo"
            return figura
        elif figura == 'T' or figura == 't':
            figura = "Triângulo"
            return figura
        elif figura == 'P' or figura == 'p':
            figura = "Trapézio"
            return figura
        elif figura == 'C' or figura == 'c':
            figura = "Círculo"
            return figura


def calcular_proporcao_percentual_das_areas(area_figura_1,area_figura_2):
    if area_figura_1>area_figura_2:
        percentual = (area_figura_2/area_figura_1)*100
    else:
        percentual = (area_figura_1/area_figura_2)*100
    return percentual


def calcular_area_circulo(pi,raio):
    area = pi*raio**2
    return area


def calcular_area_quadrado(lado_quadrado):
    area = lado_quadrado**2
    return area


def calcular_area_retangulo(comprimento_retangulo,largura_retangulo):
    area = comprimento_retangulo*largura_retangulo
    return area


def calcular_area_triangulo(base_triangulo,altura):
    area = (base_triangulo*altura)/2
    return area


def calcular_area_trapezio(base_maior_trapézio,base_menor_trapézio,altura_trapezio):
    area = ((base_maior_trapézio+base_menor_trapézio)*altura_trapezio)/2
    return area


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