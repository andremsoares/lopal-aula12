import tkinter as tk

# Funções para efeito de placeholder

def email_foco_entrou(event):
    if entrada_email.get() == "e-mail":
        entrada_email.delete(0, tk.END)
        entrada_email.config(fg="white")


def email_foco_saiu(event):
    if entrada_email.get() == "":
        entrada_email.insert(0, "e-mail")
        entrada_email.config(fg="gray")
        
def senha_foco_entrou(event):
    if entrada_senha.get() == "senha":
        entrada_senha.delete(0, tk.END)
        entrada_senha.config(
            show="*", fg="white"
        )  # Oculta os caracteres ao digitar


def senha_foco_saiu(event):
    if entrada_senha.get() == "":
        entrada_senha.config(
            show="", fg="gray"
        )  # Exibe o texto "senha" sem ocultar
        entrada_senha.insert(0, "senha")

# Instância a janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("1080x720")
janela.config(bg="white")

# Frame Container para manter tudo centralizado junto
container = tk.Frame(janela, bg="white")
container.place(relx=0.5, rely=0.5, anchor="center")

# Imagem logo
imagem_logo = tk.PhotoImage(file="images/logo tkinter.png")
rotulo_logo = tk.Label(container, bg="white", image=imagem_logo)
rotulo_logo.pack(pady=(0, 20))  # Espaçamento inferior após o logo

# Caixas de texto (com parâmetros e funções placeholder)

entrada_email = tk.Entry(
    container,
    width=32,
    font=("Arial", 12),
    bg="#eaeaea",
    bd=0,
    relief="raised",
    fg="gray"
    )
entrada_email.insert(0, "e-mail")
entrada_email.bind("<FocusIn>", email_foco_entrou)
entrada_email.bind("<FocusOut>", email_foco_saiu)
entrada_email.pack(pady=8, ipady=8)

entrada_senha = tk.Entry(
    container,
    width=32,
    font=("Arial", 12),
    bg="#eaeaea",
    bd=0,
    relief="raised",
    fg="gray"
    )
entrada_senha.insert(0, "senha")
entrada_senha.bind("<FocusIn>", senha_foco_entrou)
entrada_senha.bind("<FocusOut>", senha_foco_saiu)
entrada_senha.pack(pady=8, ipady=8)

# Botão acessar

botao_acessar = tk.Button(
    container,
    text="ACESSAR",
    width=34,
    font=("Arial", 10, "bold"),
    bd=0,
    bg="#298FC2",
    fg="white",
    relief="flat",
    cursor="hand2"
    )
botao_acessar.pack(pady=(15, 20), ipady=8)

# Link do primeiro acesso

link_primeiro_acesso = tk.Label(
    container,
    bg="white",
    fg="black",
    text="PRIMEIRO ACESSO",
    font=("Arial", 9, "bold"),
    cursor="hand2"
    )
link_primeiro_acesso.pack()

# Puxando a função janela

janela.mainloop()
