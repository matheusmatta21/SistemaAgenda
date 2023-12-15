from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox 

def escreverDados(): #sem validação
        nome = inputNome.get()
        numero = int(inputNumero.get())
        email = inputEmail.get() 
        preferencial = comboboxPreferencial.get()
        arquivo = open("contatos.txt", "a", encoding="utf-8")
        arquivo.write(f"{nome},{numero},{email},{preferencial}\n")
        arquivo.close()
    

def validarDados(): ##com validacao incompleta
        booleano = True
        nome = inputNome.get()
        numero = inputNumero.get()
        email = inputEmail.get()
        preferencial = comboboxPreferencial.get()
        if nome == '' or nome == ' ':
            messagebox.showerror(title="Erro", message="Digite um nome!")
            booleano = False
        elif numero == "" or numero == " " or numero.isnumeric() == False:
            messagebox.showerror(title="Erro", message="Digite um número!")
            booleano = False
        elif email == '' or email == " ":
            messagebox.showerror(title="Erro", message="Digite um email!")
            booleano = False
        elif "@" not in email and "." not in email:
            messagebox.showerror(title="Erro", message="Insira a formatação certa do e-mail!")
            booleano = False
        elif preferencial == "" or preferencial == " ":
            messagebox.showerror(title="Erro", message="Selecione se você faz parte do grupo preferencial!")
            booleano = False
        if booleano == True:
            escreverDados()
        else:
            pass
       
     

def lerDados():
    windowTwo = Tk() #passivel de erro
    windowTwo.title("Lista de contatos")
    windowTwo.geometry("1000x500")

    arquivo = open("contatos.txt", "r", encoding="utf-8")
    for linha in arquivo.readlines():
        contato = linha.split(",")
        labelContatos = Label(windowTwo, text=f"contato:{contato[0]},{contato[1]},{contato[2]},{contato[3]}")
        labelContatos.pack()

def limparFormulario():
    inputNome.delete(0, END)
    inputNumero.delete(0, END)
    inputEmail.delete(0, END)
    comboboxPreferencial.delete(0, END)




window = Tk()
window.title("Sistema de Agenda de Contatos")
window.geometry("600x300")

#nome

lblNome = Label(window, text="Nome:")
lblNome.pack()
inputNome = Entry(window, text="Nome", bd=2)
inputNome.pack()

#numero

lblNumero = Label(window, text="Número de telefone:")
lblNumero.pack()
inputNumero = Entry(window, bd=2)
inputNumero.pack()

#email

lblEmail = Label(window, text="Endereço de e-mail:")
lblEmail.pack()
inputEmail = Entry(window, text="Email", bd=2)
inputEmail.pack()

#preferencial

valores = ("Sim", "Nâo")
labelpreferencial = Label(window,text="Preferencial:")
labelpreferencial.pack()
comboboxPreferencial = Combobox(window, values=valores)
comboboxPreferencial.pack()

#Botões de enviar e limpar e ver contatos
btn = Button(window,text="Enviar", command=validarDados)
btn.pack()

btn2 = Button(window,text="Limpar", command=limparFormulario)
btn2.pack()

btn3 = Button(window,text="Ver contatos",command=lerDados)
btn3.pack()

window.mainloop()