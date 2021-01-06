"""
Any e All

all () - Retorna true se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio
any () - Retorna true se qualquer elemento do iteravel for verdadeiro, se o iteravel estiver vazio retorna falso

"""
# All
print(all(letra for letra in ['aeiou'] if letra in ['aei']))

# Any
print(any(letra for letra in [0, 3, 4, 5, 6] if letra in [6]))
