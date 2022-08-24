from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto("Camiseta", 50)
p2 = Produto("Iphone", 5639)
p3 = Produto("Calça", 15)

carrinho.inserir_produto(p1)

carrinho.lista_produto()
