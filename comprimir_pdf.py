import subprocess

input_pdf = "entrada.pdf"
output_pdf = "saida_comprimida.pdf"

gs_path = r"definir o caminho do Ghostgenius"  # ajuste se a versão for diferente

subprocess.call([
    gs_path,
    "-sDEVICE=pdfwrite",
    "-dCompatibilityLevel=1.4",
    "-dPDFSETTINGS=/ebook",  # /screen, /ebook, /printer, /prepress
    "-dNOPAUSE",
    "-dQUIET",
    "-dBATCH",
    f"-sOutputFile={output_pdf}",
    input_pdf
])
