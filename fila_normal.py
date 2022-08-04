from fila_base import FilaBase

class Filanormal(FilaBase):

    def geraSenhaAtual(self) -> None:
        self.senhaAtual = f'NM{self.codigo}'


    def atualizaFila(self) -> None:
        self.reseta_fila()
        self.geraSenhaAtual()
        self.fila.append(self.senhaAtual)

    def chamaCliente(self, caixa:int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')