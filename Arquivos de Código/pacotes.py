"""
Pacotes

Modulos - Apenas um arquivo Python que pode ter diversas funções para utilizarmos
Pacote - É um diretório contendo uma coleção de módulos

Obs. nas versões 2.x, um pacote deveria conter dentro dele um arquivo denominado __inity__.py
     nas versões 3.x, não é obrigatória a utilização deste arquivo, mas ainda é utilizado para manter compatibilidade

No Pycharm clica em new python package
Para utilizar um pacote dentro de um pacote, utiliza-se:

Pacote1 . Pacote2

"""

from Geek import geek1, geek2
from Geek.University import Geek3, Geek4
print(geek1.função1(2,3))
print(geek2.função2())
print(Geek3.função3())
print(Geek4.função4())