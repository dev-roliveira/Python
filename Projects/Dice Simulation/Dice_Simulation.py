import tkinter as tk
import random, os, sys

class Application:
    def __init__(self, master=None):

        self.widget1 = tk.Frame(master)
        self.widget1.pack()

        self.msg = tk.Label(self.widget1, text="Dice Simulation")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack()

        self.rodar = tk.Button(self.widget1)
        self.rodar["text"] = "Rodar Dado"
        self.rodar["font"] = ("Calibri", "9")
        self.rodar["width"] = 10
        self.rodar.bind("<Button-1>", self.mudarImagem)
        self.rodar.pack() 


    def mudarImagem(self, event):
            path = r"/home/renan/Python/Python-Essencial/Python-Essencial/geekuniversityppe/Projects/Dice Simulation/images/"
            random_filename = random.choice([x for x in os.listdir(path)if os.path.isfile(os.path.join(path,x))])
            imagem = tk.PhotoImage(file=path + random_filename)
            w = tk.Label(root, image=imagem)
            w.imagem = imagem
            w.pack()
            if self.msg["text"] == "Dice Simulation":
               self.msg["text"] = "Você tirou: "
               w.pack()
            else:
               self.msg["text"] = "Dice Simulation"
               w.pack_forget()
               python = sys.executable
               os.execl(python, python, * sys.argv)
               

root = tk.Tk()
Application(root)
root.mainloop()