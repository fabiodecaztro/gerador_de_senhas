import re as regex
import clipboard as area_de_transferencia
from random import randint as numero_aleatorio


# import os
# os.system('cls')


class GeradorDeSenhas:
    def __init__(self):

        self.senha_criada = []

    def verificador(self, quantidade_caracter, tipo_de_senha):
        self.quantidade_caracter = quantidade_caracter
        if tipo_de_senha == 1:
            return self.__senha_numerica()

    def __gera_numero(self):
        return numero_aleatorio(0, 9)

    def __senha_numerica(self):
        arrey_acumulador = []
        contador = 0

        while contador < self.quantidade_caracter:
            numero_aleatorio = self.__gera_numero()

            if numero_aleatorio not in arrey_acumulador:
                arrey_acumulador.append(numero_aleatorio)
                contador += 1

            if len(arrey_acumulador) == 10:
                arrey_de_transferencia = arrey_acumulador.copy()
                self.senha_criada.append(arrey_de_transferencia)
                arrey_acumulador.clear()

        self.senha_criada.append(arrey_acumulador)

        return self.__senha_finalizada(self.senha_criada)

    def __senha_finalizada(self, senha_criada):
        senha_finalizada = regex.sub(r'\D', '', str(senha_criada))
        area_de_transferencia.copy(senha_finalizada)
        return senha_finalizada



# aaa = GeradorDeSenhas()
# print(aaa.__gera_numero())
# print(aaa.verificador(1,1))
