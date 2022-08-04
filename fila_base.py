import abc
from typing import List

from constantes import tamanho_padrao_maximo, tamanho_padrao_minimo

class FilaBase(metaclass=abc.ABCMeta):
    codigo = 0
    fila: list[str] = []
    clientes_atendidos: list[str]  = []
    senha_atual:str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= tamanho_padrao_maximo:
            self.codigo = tamanho_padrao_minimo
        else:
            self.codigo += 1

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    @abc.abstractmethod
    def chama_cliente(self):
        ...
