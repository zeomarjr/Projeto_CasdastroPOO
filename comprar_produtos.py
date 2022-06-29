from produtos_estoque import *

class Compra:
    def __init__(self):
        self.entrada = Estoque()

    def comprar(self):
        entrada = input('Cod do produto')
        for i in range(len(self.entrada.produtosEstoque)):
            if entrada == self.entrada.produtosEstoque[i].cod:
                self.entrada.produtosEstoque[i].quant += int(input('Quantidade comprada'))