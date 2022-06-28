from produtos_estoque import *

class Menu:
    def __init__(self):
        produtos_estoque = Estoque()
        while True:
            entrada=input(('1- Cadastrar novo produto\n2- Listar Produtos Cadastrados\n3- Alterar descrição do produto\n4- Procurar produto\n0- Sair'))
            if entrada == '1':
                produtos_estoque.salvar_produtos()
            elif entrada == '2':
                produtos_estoque.listar_produtos()
            elif entrada == '3':
                produtos_estoque.alterar_produtos()
            elif entrada == '4':
                produtos_estoque.procurar_produtos()
            elif entrada == '0':
                break
            else:
                print('Opção Inválida')