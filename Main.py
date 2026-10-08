import tkinter as tk
from tkinter import messagebox
from Gerenciar_Hospedagem import listar_hospedagens, inserir_hospedagem
from Gerenciar_Hóspedes import inserir_Hóspede, listar_hóspedes
from Gerenciar_Quartos import listar_Ids_Quartos, Inserir_Quartos


def inserir_quarto():
    Inserir_Quartos()
    messagebox.showinfo("Sucesso", "Quarto inserido com sucesso!")


def inserir_hospede():
    inserir_Hóspede()
    messagebox.showinfo("Sucesso", "Hóspede inserido com sucesso!")


def inserir_hospedagem():
    inserir_hospedagem()
    messagebox.showinfo("Sucesso", "Hospedagem inserida com sucesso!")


def ver_quartos_disponiveis():
    quartos = listar_Ids_Quartos()
    if quartos:
        quartos_str = "\n".join([f"Quarto ID: {quarto}" for quarto in quartos])
        messagebox.showinfo("Quartos Disponíveis", quartos_str)
    else:
        messagebox.showinfo("Quartos Disponíveis", "Nenhum quarto disponível.")


def ver_hospedes():
    hospedes = listar_hóspedes()
    if hospedes:
        hospedes_str = "\n".join([f"Nome: {hospede[0]}, CPF: {hospede[1]}" for hospede in hospedes])
        messagebox.showinfo("Hóspedes", hospedes_str)
    else:
        messagebox.showinfo("Hóspedes", "Nenhum hóspede cadastrado.")


def ver_hospedagens():
    hospedagens = listar_hospedagens()
    if hospedagens:
        hospedagens_str = "\n".join([
            f"ID: {row[0]}, Hóspede: {row[1]}, Quarto: {row[2]}, Entrada: {row[3]}, Saída: {row[4]}"
            for row in hospedagens
        ])
        messagebox.showinfo("Hospedagens", hospedagens_str)
    else:
        messagebox.showinfo("Hospedagens", "Nenhuma hospedagem cadastrada.")


# Criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Gerenciamento do Hotel Barbosa")
janela.geometry("400x400")

# Adicionar botões para cada funcionalidade
tk.Label(janela, text="Sistema de Gerenciamento do Hotel Barbosa", font=("Arial", 14)).pack(pady=10)

tk.Button(janela, text="1. Inserir Quarto", command=inserir_quarto, width=30).pack(pady=5)
tk.Button(janela, text="2. Inserir Hóspede", command=inserir_hospede, width=30).pack(pady=5)
tk.Button(janela, text="3. Inserir Hospedagem", command=inserir_hospedagem, width=30).pack(pady=5)
tk.Button(janela, text="4. Ver Quartos Disponíveis", command=ver_quartos_disponiveis, width=30).pack(pady=5)
tk.Button(janela, text="5. Ver Hóspedes", command=ver_hospedes, width=30).pack(pady=5)
tk.Button(janela, text="6. Ver Hospedagens", command=ver_hospedagens, width=30).pack(pady=5)
tk.Button(janela, text="Sair", command=janela.quit, width=30).pack(pady=20)

# Iniciar o loop da interface
janela.mainloop()