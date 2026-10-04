from tkinter import Tk, Label, Entry, Text, Button, messagebox

# Função acionada ao clicar no botão de enviar
def enviar_formulario():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    mensagem = text_mensagem.get("1.0", "end-1c")

    # Validação simples para ver se os campos estão preenchidos
    if not nome or not email or not mensagem:
        messagebox.showerror("Erro", "Preencha os campos obrigatórios (Nome, E-mail e Mensagem)!")
        return

    # Aqui você pode processar os dados (salvar em arquivo, enviar e-mail, etc.)
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Telefone: {telefone}")
    print(f"Mensagem: {mensagem}")

    messagebox.showinfo("Sucesso", "Formulário enviado com sucesso!")

# Configuração da janela principal
janela = Tk()
janela.title("Formulário de Contato")
janela.geometry("400x500")

# Campo Nome
Label(janela, text="Nome:").pack(anchor="w", padx=30, pady=(10, 0))
entry_nome = Entry(janela, width=40)
entry_nome.pack(padx=30, pady=5)

# Campo E-mail
Label(janela, text="E-mail:").pack(anchor="w", padx=30, pady=(10, 0))
entry_email = Entry(janela, width=40)
entry_email.pack(padx=30, pady=5)

# Campo Telefone
Label(janela, text="Telefone:").pack(anchor="w", padx=30, pady=(10, 0))
entry_telefone = Entry(janela, width=40)
entry_telefone.pack(padx=30, pady=5)

# Campo Mensagem
Label(janela, text="Mensagem:").pack(anchor="w", padx=30, pady=(10, 0))
text_mensagem = Text(janela, width=30, height=6)
text_mensagem.pack(padx=30, pady=5)

# Botão Enviar
botao_enviar = Button(janela, text="Enviar", command=enviar_formulario, bg="green", fg="white", width=15)
botao_enviar.pack(pady=20)

# Iniciar a aplicação
janela.mainloop()