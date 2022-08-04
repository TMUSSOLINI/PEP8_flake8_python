from fila_normal import Filanormal
from fila_prioritaria import FilaPrioritaria

# fila_teste = Filanormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(10))

fila_teste2 = FilaPrioritaria()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(10))
print(fila_teste2.chama_cliente(1))
print(fila_teste2.estatisticas('10/01/2022', 198, 'detail'))
