"""
Modulo Collections - Counter

Collections = High Performance Container Datetypes

Counter - recebe um iteravel como parâmetro e cria um objeto do tipo collections couter que é parecido com um dicionario
contendo como chave o elemento da lista passada como parâmetro, e como valor a quantidade de ocorrências desse elemento.


"""

# Utilizando o counter
# Podemos utilizar qualquer iteravel, neste exemplo usou-se uma lista

# Exemplo 1
from collections import Counter
lista = range(1, 11)
res = Counter(lista)
# print(type(res))
print(res)

# Exemplo 2
# print(Counter('Geek University'))

# Exemplo 3
texto = """Apollo 8 foi um voo espacial tripulado norte-americano responsável pela primeira órbita ao redor da Lua. 
Esta foi a segunda missão tripulada do Programa Apollo e a primeira na história da humanidade a deixar a órbita 
terrestre baixa e retornar. Os astronautas Frank Borman, Jim Lovell e William Anders tornaram-se os primeiros humanos 
a testemunhar e fotografar um Nascer da Terra e escapar da gravidade de um corpo espacial. A Apollo 8 foi lançada em 
21 de dezembro de 1968 e foi o primeiro voo tripulado do foguete Saturno V e o primeiro tripulado a partir do Centro 
Espacial John F. Kennedy. A Apollo 8 demorou quase três dias para alcançar a Lua. A tripulação orbitou o satélite dez 
vezes no decorrer de vinte horas, no processo realizando uma transmissão televisiva na véspera de Natal, 
em que os três astronautas leram os primeiros dez versos do Gênesis. A transmissão na época foi assistida por 
milhares de pessoas ao redor do mundo. A espaçonave retornou para a Terra e amerrissou no Oceano Pacífico em 27 de 
dezembro. A missão bem-sucedida da Apollo 8 pavimentou o caminho para a Apollo 11 cumprir o objetivo nacional 
estabelecido em 1961 pelo presidente John F. Kennedy de alunissar na Lua antes do fim da década. Borman, 
Lovel e Anders foram nomeados as Pessoas do Ano pela revista Time logo depois de sua volta. """

# palavras = texto.split()
# res = Counter(palavras)
# print(res)
# print(res.most_common(5))  # Encontrando as 5 palavras com maior ocorrência no texto
