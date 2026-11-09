import tkinter as tk

janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("1080x720")
janela.config(bg="white")

# Criando cabeçalho

header = tk.Frame(janela, bg="white")
header.pack(fill="x", padx=30, pady=20)

# Frame do perfil

header_esquerdo = tk.Frame(header, bg="white")
header_esquerdo.pack(side="left")

imagem_perfil = tk.PhotoImage(file="images/profile.png")
rotulo_perfil = tk.Label(header_esquerdo, image=imagem_perfil)
rotulo_perfil.pack()

janela.mainloop()