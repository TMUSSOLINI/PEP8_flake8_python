from fila_base import FilaBase
from constantes import codigo_normal


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{codigo_normal}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop()
        self.clientes_atendidos.append(cliente_atual)
        return (f'cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')