from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: list[str]) -> dict:
        estatisticas: Dict [str, Union[list[str], str, int] ] = {}
        estatisticas['dia'] = self.dia
        estatisticas['agencia'] = self.agencia
        estatisticas['clientes atendidos'] = clientes_atendidos
        estatisticas['quantidade clientes atendidos'] = len(clientes_atendidos)

        return estatisticas