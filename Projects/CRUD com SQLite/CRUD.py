from tkinter import *
from Usuarios import Usuarios

class Crud:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.dados_do_usuario = Frame(master)
        self.dados_do_usuario["pady"] = 10
        self.dados_do_usuario.pack()

        self.nome_do_usuario = Frame(master)
        self.nome_do_usuario["padx"] = 20
        self.nome_do_usuario.pack()

        self.senha_do_usuario = Frame(master)
        self.senha_do_usuario["padx"] = 20
        self.senha_do_usuario.pack()

        self.botao_autenticar = Frame(master)
        self.botao_autenticar["pady"] = 20
        self.botao_autenticar.pack()

        self.titulo = Label(self.dados_do_usuario, text= 'Dados do Usuario')
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.nome_do_usuario, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.nome_do_usuario)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=RIGHT)

        self.senhaLabel = Label(self.senha_do_usuario, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.senha_do_usuario)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.bind('<Return>', self.verificasenha)
        self.senha.pack(side=RIGHT)

        self.autenticar = Button(self.botao_autenticar)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificasenha
        self.autenticar.pack()

        self.mensagem = Label(self.botao_autenticar, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # Metodo verificar senha
    def verificasenha(self, event):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "admin" and senha == "admin":
            Application()
        else:
            self.mensagem["text"] = "Erro na autenticacao"


root = Tk()
Crud(root)
root.geometry('500x200')
root.resizable(width=0, height=0)
root.mainloop()
