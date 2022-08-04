class FilaPrioritaria:
    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = ''

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa:int) -> str:
        cliente_atual = self.fila.pop()
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatisticas(self, dia:str, agencia:int, flag:str) -> dict:
        if flag != 'detail':
            estatisticas = {f'{agencia}-{dia}':len(self.clientes_atendidos)}
        else:
            estatisticas = {}
            estatisticas['dia'] = dia
            estatisticas['agencia'] = agencia
            estatisticas['clientes atendidos'] = self.clientes_atendidos
            estatisticas['quantidade clientes atendidos'] = len(self.clientes_atendidos)

        return estatisticas