from models.produtosModel import Produto

class ClienteModel(Produto):
    
    def __init__(self, banco):
        super().__init__(banco) 
        self.table = 'produtos' 
        self.columns = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'nome': 'TEXT NOT NULL',
            'quantidade': 'INTEGER',
            'preco': 'FLOAT'
            
        } 
        self.create_table(self.table, self.columns) 
    

    def inserir_produto(self, id, nome, quantidade, preco):
        values = {
            'id': id,
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco,
        }
        return self.inserir(self.table, values)
    
    

    def listar_clientes(self):
        return self.select_all(self.table)
    
    

    def buscar_produto(self, produto_id):
        condition = {'where': f'id = {produto_id}'}
        return self.select(self.table, condition)
    
    
    def atualizar_produto(self, produto_id, nome=None, quantidade=None, preco=None):
        values = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco,
        } 
        condition = {
            'where': f'id = {produto_id}'
        } 
        return self.update(self.table, values, condition) 

    def deletar_produto(self, produto_id):
        condition = {
            'where': f'id = {produto_id}'
        }
        return self.delete(self.table, condition)