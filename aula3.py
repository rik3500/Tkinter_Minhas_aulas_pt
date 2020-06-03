###Botoes

from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_widgets()
        # criando o Loop
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= '#1e3743')
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=300)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        #self.frame_1.place(x=50, y=50, width=100, height=100)
        #self.frame_1.pack(side="top")

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    ##########
    def criando_widgets(self):


        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text= 'Limpar', bg = '#107db2', fg = 'white')
        self.bt_limpar.place(relx=0.14, rely=0.08, relwidth=0.1, relheight=0.14)

        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar' , bg = '#107db2', fg = 'white')
        self.bt_buscar.place(relx=0.26, rely=0.08, relwidth=0.1, relheight=0.14)

        ### Criação do botao novo
        self.bt_novo = Button(self.frame_1, text='Novo' , bg = '#107db2', fg = 'white')
        self.bt_novo.place(relx=0.5, rely=0.08, relwidth=0.1, relheight=0.14)

        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar' , bg = '#107db2', fg = 'white')
        self.bt_alterar.place(relx=0.62, rely=0.08, relwidth=0.1, relheight=0.14)

        ### Criação do botao apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar' , bg = '#107db2', fg = 'white')
        self.bt_apagar.place(relx=0.74, rely=0.08, relwidth=0.1, relheight=0.14)

        


Application()

