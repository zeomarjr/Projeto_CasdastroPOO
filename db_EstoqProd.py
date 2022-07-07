import mysql.connector
from cadastro_produtos import Cadastro

class DBProdutos:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'q1w2e3',
            database = 'produtos'
        )
        self.meu_cursor = self.conexao.cursor()

    def salva_produtos (self, cod, nome, fab, quant):
        obj_produtos = Cadastro(cod, nome, fab, quant)
        comando_sql = f'insert into Cadastro ' \
                      f'(nome, fab, quant)value' \
                      f'("{obj_produtos.nome}", "{obj_produtos.fab}", "{obj_produtos.quant}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def lista_produtos (self):
        comando_sql = f'select * from Cadastro'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_produtos (self, nome, novo_nome, cod):
        comando_sql = f'update Cadastro set {nome} = "{novo_nome}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def procurar_produtos (self):
        pass

    def excluir_produtos (self, cod):
        comando_sql = f'delete from Cadastro where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()