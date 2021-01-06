# 01
# A = [1, 0, 5, -2, -5, 7]
# B = sum([A[0], A[1], A[5]])
# print(B)
# A.insert(4, 100)
# for valor in A:
#    print(valor)

# 02
# i = 0
# lista = []
# while i < 6:
#    valor = int(input(f'Digite o {i+1}º numero inteiro: '))
#    lista.insert(i, valor)
#    i += 1
# print(f' Os números digitados são {lista}')

# 03
# i = 0
# valor = []
# valor2 = []
# while i < 10:
#    val = float(input(f'Digite o {i+1}/10 valor: '))
#    valor.insert(i, val)
#    valor_calc = val*val
#    valor2.insert(i, valor_calc)
#    i += 1
# print(valor)
# print(valor2)

# 04
# i = 0
# val = []
# while i < 8:
#    valor = int(input(f'Digite o {i+1}/8 valor: '))
#     val.insert(i, valor)
#    i += 1
# x = int(input('Digite o primeiro índice: '))
# y = int(input('Digite o segundo índice: '))
# print(f'A  Soma dos índices é {sum([val[x], val[y]])}')

# 05
# i = 0
# val = []
# while i < 8:
#    numeros = int(input(f'Insira o {i+1}º valor para verificação: '))
#    if numeros % 2 == 0:
#        val.insert(i, numeros)
#    i += 1
# print(val)

# 07
# numero = range(1, 11)
# lista = list(numero)
# print(lista)
# print(max(lista))
# print(lista.index(max(lista)))

# 08
# val = list(range(1, 7))
# val.reverse()
# print(val)

# 09
# i = 0
# val = []
# while len(val) < 6:
#    if i % 2 == 0:
#        val.append(i)
#    i += 1
# val.reverse()
# print(val)

# 13
# i = 0
# val = []
# while len(val) < 5:
#    val.append(i)
#    i += 1
# print(val.index(max(val)))
# print(val.index(min(val)))

# 14
# valor = [1, 12, 12, 3, 12, 45, 3, 4, 12, 1]
# for n in valor:
#     count = valor.count(n)
#    if count > 1:
#        print(f'{n} aparece {count} vezes')
#        del (valor[0: (count-1)])

# 15
# i = 0
# lista = []
# while i < 4:
#    ent = input('Digite o numero: ')
#    lista.extend(ent)
#    i += 1
# lista = set(lista)
# print(lista)

# 16


# def programa():
#    i = 0
#    lista = []
#    while i < 5:
#        ent = float(input(f'Digite o {i+1}/5 número: '))
#        lista.append(ent)
#        i += 1
#    cod = int(input('Digite agora o seu Código: '))
#    if cod == 1:
#        print(lista)
#    elif cod == 2:
#        lista.reverse()
#        print(lista)
#    elif cod == 0:
#        exit(0)
#   else:
#       print('Comando invalido')
#       programa()


# programa()

# 17
# vetor = []
# for valor in range(10):
#    ent = float(input('Digite o valor: '))
#    if ent < 0:
#        vetor.append(0)
#    else:
#        vetor.append(ent)
# print(vetor)

# 18
# vetor = []
# i = 0
# for v in range(5):
#    vetor.append(int(input(f'Digite o Vetor {[v]}: ')))
# con = int(input('Digite o numero para verificação: '))
# print(vetor)
# for item in vetor:
#    if item % con == 0 or con % item == 0:
#        print(item)

# 19
# vetor = []
# for i in range(5):
#    res = (i + 5 * i) % (i + 1)
#    vetor.append(res)
# print(vetor)

# 20
# i = 0
# vetor = []
# vetor2 = []
# while i < 10:
#    res = int(input(f'Digite o {i+1} valor de 10: '))
#    if res <= 50:
#        vetor.append(res)
#    i += 1
# for valor in vetor:
#    if valor % 2 == 1:
#        vetor2.append(valor)
# print(f'Vetor 1 = {vetor} Vetor ímpar = {vetor2}')

# 21
# C = []
# for valor in range(10):
#    A = int(input(f'Digite o {valor + 1} Valor do Vetor A: '))
#    B = int(input(f'Digite o {valor + 1} valor do Vetor B: '))
#    C.append(A-B)
# print(C)

# 22
