class ProdutoView:

    def exibir_menu(self):
        print("1_cadastrar_produto")
        print('2_visualizar_produto')
        print('3_consutar_produto')
        print('4_ exibir_quantidade')
        print('5_atualizar_produto')
        print('6_excluir_produto')
        print('0_Sair')

        return input('Escolha uma opcao')

    def exibir_quantidade(self, produto):
        if not produto:
            print('Nehum produto encontrado')
        else:
            for p in produto:
                print(f'Produto: {p.nome}|preço: R${p.preco:.2f}')

    def obter_dados_produto(self):
        id = int(input('id do produto'))
        nome = input('Nome do produto')
        preco = float(input('Preco do produto'))
        quantidade = int(input('quantidade do produto'))

        return  id, nome, preco, quantidade  

    def obter_id_produto(self):
            
            return int(input("ID do produto: ")) 

    def mostrar_mensagem(self, mensagem):
        
        print(f"\n{mensagem}\n")