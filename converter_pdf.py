import os

from docx2pdf import convert

# Caminho da pasta com seus arquivos .docx
caminho_pasta = r"colocar o caminho para salvar o PDF"

# Converte todos os arquivos .docx da pasta
convert(caminho_pasta)
