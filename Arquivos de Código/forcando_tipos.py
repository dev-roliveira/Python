"""
Forcando tipos de dados com decoradores


"""

def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args=[]
            for(valor, tipo) in zip(args,tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador


@forca_tipo(str, int)
def repete_mensagem(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_mensagem('hey', '3')
