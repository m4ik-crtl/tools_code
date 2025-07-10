import os
import zipfile

from PyPDF2 import PdfReader, PdfWriter

# Caminho para o arquivo PDF original
pdf_path = "exemplo.pdf"

# Lista de capítulos: (Título, Página Inicial)
chapters = [
    ("Apresentação", 6),
]

# Criar pasta de saída
output_folder = "capitulos_pdf"
os.makedirs(output_folder, exist_ok=True)

# Ler o PDF original
reader = PdfReader(pdf_path)

# Separar os capítulos
for i, (title, start_page) in enumerate(chapters):
    end_page = chapters[i + 1][1] if i + 1 < len(chapters) else len(reader.pages)
    chapter_num = f"{i + 1:02d}"
    safe_title = "".join(c for c in title if c.isalnum() or c in " _-").strip()
    filename = f"{chapter_num} - {safe_title}.pdf"
    output_path = os.path.join(output_folder, filename)

    writer = PdfWriter()
    for p in range(start_page, end_page):
        writer.add_page(reader.pages[p])
    with open(output_path, "wb") as f:
        writer.write(f)

# Criar arquivo ZIP
zip_filename = "exemplo.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in sorted(os.listdir(output_folder)):
        file_path = os.path.join(output_folder, file)
        zipf.write(file_path, arcname=file)

print(f"\n✅ Capítulos salvos em: {output_folder}")
print(f"📦 ZIP criado: {zip_filename}")
