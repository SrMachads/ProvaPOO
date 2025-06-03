from models.produtosModel import Produto 

class ControleEstoque:
    
    def __init__(self, banco):

        self.produto_model = Produto(banco) 
    def cadastrar_produto(self, id, nome, quantidade, preco):
       
        return self.Produto_model.inserir_produto(id, nome, quantidade, preco) 

    def visualizar_produtos(self):
        
        return self.Produto_model.listar_produto() 
    def consutar_produto(self, produto_id):
        
        return self.Produto_model.buscar_produto(produto_id) 

    def atualizar_produto(self, produto_id, nome=None, quantidade=None, preco=None):
       
        return self.Produto_model.atualizar_produto(produto_id, nome, quantidade, preco) 
    def excluir_produto(self, cliente_id):
      
        return self.Produto_model.deletar_produto(cliente_id) 
    
    def exibir_quantidade(self, quantidade):
        while True:
            try:
                quantidade = int(input('insira a quantidade'))
                if quantidade >= 0:
                    print(f"A quantidade e: {quantidade}")
                    break
                else:
                    print('NAo pode ser negativa. Insira novamente')
            except ValueError:
                print('insira novamente')
