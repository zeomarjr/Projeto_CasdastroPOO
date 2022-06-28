from cadastro_produtos import *

class Estoque:
    def __init__(self):
        self.produtosEstoque = []

    def salvar_produtos(self):
        self.produtosEstoque.append(Cadastro())

    def listar_produtos(self):
        for i in range(len(self.produtosEstoque)):
            print('Cod:', self.produtosEstoque[i].cod,
                  '- Nome:', self.produtosEstoque[i].nome,
                  '- Fabricante:', self.produtosEstoque[i].fab,
                  '- Quantidade:', self.produtosEstoque[i].quant)

    def procurar_produtos(self):
        pesquisa = input('Listar produto por código :')
        for i in range(len(self.produtosEstoque)):
            if pesquisa == self.produtosEstoque[i].cod:
                print('Cod:', self.produtosEstoque[i].cod,
                      '- Nome:', self.produtosEstoque[i].nome,
                      '- Fabricante:', self.produtosEstoque[i].fab,
                      '- Quantidade:', self.produtosEstoque[i].quant)

    def alterar_produtos(self):
        modificar = input('Qual o Código do produto que deseja alterar ? ')
        for i in range(len(self.produtosEstoque)):
            if modificar == self.produtosEstoque[i].cod:
                self.produtosEstoque[i].nome = input('Alterar nome do produto:')