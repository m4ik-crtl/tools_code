import os
import tkinter as tk
from tkinter import filedialog, messagebox

from docx2pdf import convert


def selecionar_pasta(titulo="Selecione uma pasta"):
    """Abre o explorador de arquivos para escolher uma pasta"""
    pasta = filedialog.askdirectory(title=titulo)
    return pasta

def converter_docx_para_pdf():
    # Seleciona pasta de entrada
    pasta_entrada = selecionar_pasta("Selecione a pasta com os arquivos DOCX")
    if not pasta_entrada:
        messagebox.showwarning("Aviso", "Nenhuma pasta de entrada selecionada.")
        return

    # Seleciona pasta de saída
    pasta_saida = selecionar_pasta("Selecione a pasta onde salvar os PDFs")
    if not pasta_saida:
        messagebox.showwarning("Aviso", "Nenhuma pasta de saída selecionada.")
        return

    try:
        convert(pasta_entrada, pasta_saida)
        messagebox.showinfo("Sucesso", f"Conversão concluída!\nArquivos salvos em:\n{pasta_saida}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro:\n{e}")

# Interface gráfica simples
root = tk.Tk()
root.withdraw()  # Oculta a janela principal
converter_docx_para_pdf()
