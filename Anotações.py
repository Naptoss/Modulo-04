"""

Tipos de dados 
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/false 10 == 10


+,  - soma
-,  - subtração
*,  - multiplicação
/,  - divisão
//, - divisão inteira
**, - exponenciação
%,  - resto da divisão
()  - 


:s - Texto (strings)
:d - inteiros (int)
:f - pontos flutuantes (float)
:.(NUMERO)f - Quantidades de casa decimais (float) :.2f
:(CARACTERE)(> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - esquerda
< - direita
^ - meio 


variavel = 'alguma str'
print(variavel.lower()) - todo minusculo
print(variavel.uper()) - todo maisculo
print(variavel.title()) - as primeiras letras de cada nome são maiusculas
varial_qtd = len(nome) - pra puxar quantidade de caracteres do nome


if - primeiro a ser puxado
elif - puxado quando o resultado for false
else - quando não houver um elif e o if nao for puxado ele ira dar o resultado(obs: o else nao precisa ser acompanhado de alguma função, apenas com dois ponto(:) )


Continue - pula para o proximo laço 
Break - Termina a ação


Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - retorna um objeto iterável # iteráveis

def - definir um parametro 
return - retornar o valor
 *args - definido como um valor x pela comunidade
**kwargs - procura por uma key
Tuplas - a tupla nao consegue editar a lista 
lambda - função anonima, pode ser usada para organizar lista e etc; 

exemplo:
lista = [
    ['P1',5],
    ['P2',54],
    ['P3',12],
    ['P4',10],
    ['P5',19],
    ['P6',11],
    ['P7',23],
]



lista.sort(key=lambda item: item[1], reverse=True)  #<----- aqui ela esta ordenando do maior para o menor, caso queira fazer o inverso basta retirar o reverse
print(lista).

Outro exemplo:

def func(item):   <---- Definiu o item 
    return item[1]        <---- retornou o item 1        

lista.sort(key=func, reverse=True)  <----- Ordenou 
print(lista)

Outro exemplo:

print(sorted(lista, key=lambda i: i[1]))

OBS IMPORTANTE! :


d1 = {'chave1':'valor da chave'}
d1['nova chave'] = 'Valor da nova chave'

print(d1['chave1']) <--- Tudo que estiver entre cochete vai ser o valor que o requerente quer 

add - adiciona
update - atualizar
clear - limpar
discard - discartar 
union - une
intersection & - todos os elementos presentes nos dois sets
difference - elementos apenas no set da esquerda
symmetric_diference ^ - elementos que estao nos dois sets, mas nao em ambos
List Comprehension = List Comprehension foi concebida na PEP 202 e é uma forma concisa de criar e manipular listas.

Objeto iteravel - no python um objeto e considerado iteravel se ele implementa o metodo "__inter__", permitindo, por exemplo, que um loop for seja executado sobre ele.

Combinations - Permutations e Product - Itertools
Combinação - ordem não importa
Permutação - Ordem Importa 
Ambos não repetem valores unicos
Produto - Ordem importa e repete valores unicos

Python Orientado a Objetos - POO

Metodo - E simplesmente uma função que pertence a uma classe.
Os objetos são independentes um dos outros 

PascalCase - 
significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las, 
como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. 
Essa á a convenção utilizada para classes em Python;

camelCase - a única diferença de camelCase para PascalCase é a primeira letra. 
Em camelCase a primeira letra sempre será minúscula e o restante das palavras deverá iniciar com letra maiúscula. 
Como em: minhaFuncao, funcaoDeSoma, etc... Essa conversão não é usada em Python 

snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe. 
Todas as letras serão minúsculas e separadas por um underline, 
como em: minha_variavel, funcao_legal, soma.

Oque são dataclasses ?: O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.

"""
