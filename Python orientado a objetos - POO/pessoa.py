# quando uma função esta dentro de uma classe ela se torna um metodo da classe

from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, andar=False, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.andando = andar

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_comer(self):
        # print(self.comendo)
        if not self.comendo:
            print(f"{self.nome} nao está comendo. ")
            return
        print(f'{self.nome} Parou de comer.')
        self.comendo = False

    def comer(self, alimento):
        print(f"{self.nome} está comendo {alimento}")
        self.comendo = True
        return
        if self.comendo:
            print(f"{self.nome} já está comendo.")

    def andar(self, local):
        print(f"{self.nome} está andando na {local}")
        self.andando = True

    def parar_de_andar(self):
        if not self.andando:
            print(f"{self.nome} cansou de andar ")
            return
        print(f"{self.nome} esta parado ")
        self.andando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
