"""
Módulo Collections - Deque

Deque é uma lista de alta performance.

"""

from collections import deque
# Criação

deq = deque('geek')
print(deq)

# Adicionando Elementos
deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('k')  # Adiciona no começo
print(deq)

# Remoção
print(deq.pop())
print(deq.popleft())
