class Filanormal:
    codigo = 0
    fila = []
    clientesAtendidos = []
    senhaAtual:str = ''

    def geraSenhaAtual(self) -> None:
        self.senhaAtual = f'NM{self.codigo}'

    def resetaFila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizaFila(self) -> None:
        self.resetaFila()
        self.geraSenhaAtual()
        self.fila.append(self.senhaAtual)

    def chamaCliente(self, caixa:int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.clientesAtendidos.append(cliente_atual)
        return (f'cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')