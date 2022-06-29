from produtos_estoque import *
from comprar_produtos import *

class Menu:
    def __init__(self):
        produtos_estoque = Estoque()
        compra = Compra()
        compra.entrada = produtos_estoque

        while True:
            entrada=input(('1- Cadastrar novo produto\n2- Listar Produtos Cadastrados\n3- Alterar descrição do produto\n4- Procurar produto\n5- Comprar produtos\n0- Sair\n'))
            if entrada == '1':
                produtos_estoque.salvar_produtos()
            elif entrada == '2':
                produtos_estoque.listar_produtos()
            elif entrada == '3':
                produtos_estoque.alterar_produtos()
            elif entrada == '4':
                produtos_estoque.procurar_produtos()
            elif entrada == '5':
                compra.comprar()
            elif entrada == '0':
                break
            else:
                print('Opção Inválida')