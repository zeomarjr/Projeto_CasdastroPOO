class Cadastro:
    def __init__(self):
        self.cod = input('Código do produto:')
        self.nome = input('Descrição do produto:')
        self.fab = input('Fabricante do produto:')
        self.quant = int(input('Quantidade do produto:'))
        print('Produto cadastrado com sucesso!! =D')