from controllers.produtoController import ControleEstoque
from views.produtoView import ProdutoView

def main():
    
    controller = ControleEstoque('produtos.db') 
    view = ProdutoView() 

    while True:
        
        opcao = view.exibir_menu() 

        match opcao: 
            case "1":
                
                id, nome, quantidade, preco  = view.obter_dados_produto()
                controller.visualizar_produtos( id, nome, quantidade, preco) 
                view.mostrar_mensagem("Cliente cadastrado com sucesso!") 
            
            case "2":
               
                produtos = controller.listar_() 
                view.visualizar_produtos(produtos) 
            
            case "3":

                produto_id = view.obter_id_produto() 
                nome = view.obter_dados_produto() 
                controller.consutar_produto(produto_id=nome)
                view.mostrar_mensagem("Produto consultado com sucesso!")
            
            case "4":

                quantidade = view.obter_dados_produto()
                controller.visualizar_produtos(quantidade) 
                view.mostrar_mensagem("Sua quantidade é!") 

            case "5":
               
                produto_id = view.obter_id_produto() 
                nome = view.obter_dados_produto() 
                controller.atualizar_produto(produto_id=nome) 
                view.mostrar_mensagem("Produto atualizado com sucesso!") 

            case "6":
              
                produto_id = view.obter_id_produto()
                controller.excluir_produto(produto_id) 
                view.mostrar_mensagem("Produto deletado com sucesso!") 

            case "0":
                
                view.mostrar_mensagem("Encerrando o programa...") 
                break

            case _:
                
                view.mostrar_mensagem("Opção inválida, tente novamente.") 

if __name__ == "__main__": 
    main() 