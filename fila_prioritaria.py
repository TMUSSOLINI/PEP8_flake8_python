from typing import Dict, List, Union

from fila_base import FilaBase
from constantes import codigo_prioritatio
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{codigo_prioritatio}{self.codigo}'

    def chama_cliente(self, caixa:int) -> str:
        cliente_atual = self.fila.pop()
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatisticas(self,
     retorna_estatistica: Classes) -> dict:

        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)