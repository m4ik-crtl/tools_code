import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter
import os

def selecionar_e_unir():
    # 1. Configurar a janela oculta do Tkinter
    root = tk.Tk()
    root.withdraw() # Esconde a janela principal
    root.attributes('-topmost', True) # Faz a janela de seleção aparecer na frente

    # 2. Abrir menu de seleção de arquivos
    print("Abrindo menu de seleção...")
    arquivos = filedialog.askopenfilenames(
        title="Selecione os PDFs para unir",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )

    if not arquivos:
        print("Nenhum arquivo selecionado.")
        return

    # 3. Escolher onde salvar o resultado
    caminho_saida = filedialog.asksaveasfilename(
        title="Salvar como...",
        defaultextension=".pdf",
        filetypes=[("Arquivo PDF", "*.pdf")],
        initialfile="PDF_Unido.pdf"
    )

    if not caminho_saida:
        print("Operação cancelada pelo usuário.")
        return

    # 4. Processo de união
    try:
        merger = PdfWriter()
        
        for pdf in arquivos:
            print(f"Adicionando: {os.path.basename(pdf)}")
            merger.append(pdf)

        with open(caminho_saida, "wb") as f_saida:
            merger.write(f_saida)
        
        merger.close()
        
        messagebox.showinfo("Sucesso", f"PDF salvo com sucesso em:\n{caminho_saida}")
        print("Concluído!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao unir os arquivos:\n{e}")

if __name__ == "__main__":
    selecionar_e_unir()