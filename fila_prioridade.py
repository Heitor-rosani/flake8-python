class FilaPrioridade:
    codigo: int = 0
    fila = []
    cliente_atendidos = []
    senha_atual: str = ''

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PM {self.codigo}'

    def reseta_senha(self):
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self):
        self.reseta_senha()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.cliente_atendidos.append(cliente_atual)
        return f'Clinte {cliente_atual} ao caixa {caixa}'

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}: {len(self.cliente_atendidos)}'}
        else:
            estatistica = {'dia': dia, 'agencia': agencia, 'clinete_atendidos': self.cliente_atendidos,
                           'quantidade': len(self.cliente_atendidos)}

        return estatistica
