from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import tipo_fila_normal, tipo_fila_prioritaria


class FabricaFila:
    def pega_fila(tipo_fila) -> [FilaNormal, FilaPrioritaria]:
        if tipo_fila == tipo_fila_normal:
            return FilaNormal()
        elif tipo_fila == tipo_fila_prioritaria:
            return FilaPrioritaria()
        else: 
            raise NotImplementedError("Tipo de fila não existe")