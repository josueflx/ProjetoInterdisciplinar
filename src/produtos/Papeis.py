# -*- uncoding: utf-8 -*-

# Classe com o objetivo de cadastro de um produto do tipo papel

# Variaveis Globais
from produtos.Produto import Produtos # importando classe produtos do arquivo produto
arquivo = open("papeis.txt", "a") # criando variavel de escrita em arquivo de texto

class Papel(Produtos):

    def __init__(self, gramatura, formato, textura, tipo, marca, preco): # criando construtor da classe
        super().__init__(marca, preco) # instanciando os atributos da classe mae
        self._gramatura = gramatura # instanciando atributos da propria classe
        self._formato = formato
        self._textura = textura
        self._tipo = tipo

    def cadastro(self):
        lista = (super(Papel, self).cadastro(self))
        gramatura = float(input("Informe a gramatura do papel: "))
        formato = input("Informe o formato do papel: ")
        textura = input("Informe a textura do papel: ")
        tipo = input("Informe o tipo do papel: ")

        p = Papel(gramatura, formato, textura, tipo, lista[0], lista[1]) # passando os valores como parametros

        papel = (p.marca, gramatura, formato, textura, tipo, p.preco)# criando uma lista com as informações ]
                                                                    # inseridas pelo usuario

        arquivo.write(str(papel) + "\n")# convertendo a lista para uma string e armazenando em um arquivo de texto
        print("\nPapel Cadastrado com Sucesso!\n")

    # get e set
    @property
    def gramatura(self):
        return self._gramatura

    @property
    def formato(self):
        return self._formato

    @property
    def textura(self):
        return self._textura

    @property
    def tipo(self):
        return self._tipo
