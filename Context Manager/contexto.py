class Arquivo:
    def __init__(self, arquivo, modo):
        print("INIT")
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print("Entrou na classe")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saiu da Classe")
        self.arquivo.close()


with open('abc.text', 'w') as arquivo:
    arquivo.write("Macacos são legais")
