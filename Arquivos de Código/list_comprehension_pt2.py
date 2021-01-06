"""
List Comprehension Parte 2

Pode-se adicionar estruturas condicionais lógicas às List Comprehension

"""
# Exemplo 1
'Qualquer numero par, modulo de 2 o resultado será zero, e zero em Python é False. (Not False == True)'
'Qualquer numero impar, modulo de 2 o resultado será um, e um em Python é True.'

# numeros = [1, 2, 3, 4, 5, 6]
# print(f'{[numero for numero in numeros if not numero % 2]} = par')
# print(f'{[numero for numero in numeros if numero % 2]} = impar')

# Exemplo 2
# numeros = [1, 2, 3, 4, 5, 6]
# print([numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros])
