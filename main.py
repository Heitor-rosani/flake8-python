from fila_normal import FilaNormal
from fila_prioridade import FilaPrioridade


fila_teste = FilaPrioridade()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(1))
print(fila_teste.chama_cliente(2))
print(fila_teste.chama_cliente(3))
print(fila_teste.chama_cliente(4))
print(fila_teste.estatistica('22/02/2021', 628, 'detail'))
# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(11))
# print(fila_teste.chama_cliente(10))
# print(fila_teste.chama_cliente(5))