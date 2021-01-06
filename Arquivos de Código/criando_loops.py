"""
Criando a própria versão de Looṕ

for num in [1,2,3,4,5]:
    print(num)
"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Khal Drogo')
