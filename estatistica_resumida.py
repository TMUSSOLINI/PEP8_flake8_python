from typing import List, Dict, Union


class EstatisticaResumida:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: list[str]) -> dict:
        estatisticas: Dict [str, Union[list[str], str, int] ] = {}
        estatisticas[f'{self.agencia} - {self.dia}'] = len(clientes_atendidos)

        return estatisticas