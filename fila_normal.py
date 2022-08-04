from fila_base import FilaBase


class Filanormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senhaAtual = f'NM{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')