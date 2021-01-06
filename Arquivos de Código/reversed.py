"""
Reversed
reversed() inverte o iteravel

- Não confundir com a função reverse().
- reversed() funciona em qualquer iteravel.

Obs. reversed() retorna um objeto do tipo list_reverseiterator
Obs2. Podemos converter o elemento posteriormente em uma tupla, lista ou conjunto
Obs3. Set não tem ordem definida

"""

lista = (1, 2, 3, 4, 5, 6, 7, 8)
print(set(reversed(lista))) # Set não tem ordem definida
print(tuple(reversed(lista)))
print(list(reversed(lista)))

'Iterando em reversed()'
# for letra in reversed('Sansa Stark'):
#    print(letra, end='')

'Iterando sem o for'
# print(''.join(list(reversed('Sansa Stark'))))

'Loop reverso'
# for n in reversed(range(0, 10)):
#    print(n)

