from db_EstoqProd import DBProdutos

class DB_Menu:
    def __init__(self):
        produtos = DBProdutos()

        while True:
            entrada_menu = input('Digite:\n'
                                 '1 - Cadastrar novo produto\n'
                                 '2 - Listar produtos\n'
                                 '3 - Alterar descriçao do produto\n'
                                 '4 - Procurar produtos\n'
                                 '5 - Comprar produtos\n'
                                 '0 - Sair\n')

            if entrada_menu == '1':
                cod = None
                nome = input('Entre com o nome: ')
                fab = input('Fabricante do produto: ')
                quant = input('Quantidade do produto: ')
                produtos.salva_produtos(cod, nome, fab, quant)

            elif entrada_menu == '2':
                produtos.lista_produtos()

            elif entrada_menu == '3':
                cod = int(input('Informe o código do produto: '))
                novo_nome = input('Entre com o novo nome: ')
                nome = 'nome'
                produtos.alterar_produtos(nome, novo_nome, cod)

            elif entrada_menu == '4':
                pass

