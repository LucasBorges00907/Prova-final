def main():


    produtos = {}
    comandas = {}
    itens = {}
    
    arquivo_produtos = open("produtos.txt",'r',encoding='utf-8')
    linhas_produtos = arquivo_produtos.readlines()
    for linha in linhas_produtos:
        id_produto, nome_produto, valor_produto = linha.strip().split(";")
        produtos[id_produto] = {"nome": nome_produto, "valor": float(valor_produto)}
    
    arquivo_comandas = open("comandas.txt",'r', encoding='utf-8')
    linhas_comandas = arquivo_comandas.readlines()
    for linha in linhas_comandas:
            id_comanda, itens_comanda = linha.strip().split(":")
            comandas[int(id_comanda)] = {"numero": int(id_comanda), "itens": {}}
            for item_id in itens_comanda.split(","):
                comandas[int(id_comanda)]["itens"][int(item_id)] = int(item_id)


    arquivo_itens = open("itens.txt",'r', encoding='utf-8')
    linhas_itens = arquivo_itens.readlines()
    for linha in linhas_itens:
        item_id, produto_id, comanda_id, quantidade_item = linha.strip().split(",")
        itens[int(item_id)] = {"id": int(item_id), "produto_id": produto_id, "comanda_id": int(comanda_id), "quantidade": int(quantidade_item)}


def cadastrar_produto(produtos):
    id_produto = obter_texto("Digite o ID do produto: ")
    nome_produto = obter_texto("Digite o nome do produto: ")
    valor_produto = obter_numero_positivo("Digite o valor do produto: ")
    produtos[id_produto] = {"nome": nome_produto, "valor": valor_produto}

def gerar_comanda(comandas):
    tamanho = len(comandas)
    id_comanda = tamanho + 1
    comandas[id_comanda] = {"numero": id_comanda, "itens": {}}

def adicionar_item(comandas,produtos,itens):
    id_comanda = obter_numero_positivo("Digite o ID da comanda: ")
    id_produto = obter_texto("Digite o ID do produto: ")
    quantidade_item = obter_numero_positivo("Digite a quantidade do item: ")
    for id in comandas:
        if id_comanda != id:
            mostrar_texto("Comanda não encontrada.")
        return
    for id_pro in produtos:
        if id_pro != id_produto:
            mostrar_texto("Produto não encontrado.")
        return
    item_id = len(itens) + 1
    itens[item_id] = {"id": item_id, "produto_id": id_produto, "comanda_id": id_comanda, "quantidade": quantidade_item}
    comandas[id_comanda]["itens"][item_id] = item_id

def mostrar_cardapio(produtos):
    print("Cardápio:")
    for produto in produtos:
        print(f"{produto['nome']} - R$ {produto['valor']}")

def mostrar_itens_comanda(comandas,itens,produtos):
    id_comanda = obter_numero_positivo("Digite o ID da comanda: ")
    for id in comandas:
        if id != id_comanda:
            print("Comanda não encontrada.")
        return
    total_valor_itens = 0
    for item_id in comandas[id_comanda]["itens"]:
        item = itens[item_id]
        produto = produtos[item["produto_id"]]
        valor_item = produto["valor"] * item["quantidade"]
        total_valor_itens = total_valor_itens + valor_item
        print(f"{produto['nome']} - {item['quantidade']} x R$ {produto['valor']} = R$ {valor_item}")
    print(f"Total da comanda: R$ {total_valor_itens}")


def pagar_comanda(comandas,itens,produtos):
    id_comanda = int(input("Digite o ID da comanda: "))
    for id_c in comandas:
        if id_comanda != id_c:
            print("Comanda não encontrada.")
        return
    total_valor_itens = 0
    for item_id in comandas[id_comanda]["itens"]:
        item = itens[item_id]
        produto = produtos[item["produto_id"]]
        valor_item = produto["valor"] * item["quantidade"]
        total_valor_itens = total_valor_itens + valor_item
    print(f"Total a pagar: R$ {total_valor_itens}")
    del comandas[id_comanda]
    
def tornar_comanda_vazia(comandas):
    id_comanda = int(input("Digite o ID da comanda: "))

    if id_comanda: 
        for id in comandas:
         if id != id_comanda:
            print("Comanda não encontrada.")


def mostrar_total_vendido(itens,produtos):
    total_vendido = 0
    for item in itens:
        produto = produtos[item["produto_id"]]
        valor_item = produto["valor"] * item["quantidade"]
        total_vendido += valor_item
    print(f"Total vendido: R$ {total_vendido}")





def obter_numero(label = 'Digite um número: '):
    numero = input(label)
    while not eh_numero(numero) or numero == '':
        mostrar_texto ("Valor inválido!")
        numero = input(label)
    numero = int(numero)
    return numero


def obter_numero_positivo (label = "Digite um número: "):
    numero = input(label)
    while not eh_numero(numero) or numero == '':
        mostrar_texto ("Valor inválido!")
        numero = input(label)
    numero = int(numero)
    if numero > 0:
        return numero
    else:
        mostrar_texto("O número deve ser positivo!")
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

