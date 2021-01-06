"""
Estruturas Logícas

and -> Operador Binário, ambos precisam ser verdadeiros

or -> Operador Binário, apenas um precisa ser verdadeiro

not -> Operador Unário, o valor booleano é invertido

is -> Operador Binário, comparação de valores
"""
ativo = False
logado = True

if ativo and logado:
    print('Bem Vindo')
else:
    print('Você precisa ativar sua conta, por favor cheque seu e-mail')
