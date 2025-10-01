# Ferramentas de Automação para PDFs e Documentos

Este repositório contém uma coleção de scripts Python para automatizar tarefas comuns com arquivos PDF e DOCX, como compressão, conversão e divisão de documentos.

## Índice

- [Pré-requisitos Gerais](#pré-requisitos-gerais)
- [1. Comprimir PDF](#1-comprimir-pdf)
  - [Descrição](#descrição)
  - [Pré-requisitos](#pré-requisitos)
  - [Como Usar](#como-usar)
- [2. Converter DOCX para PDF](#2-converter-docx-para-pdf)
  - [Descrição](#descrição-1)
  - [Pré-requisitos](#pré-requisitos-1)
  - [Como Usar](#como-usar-1)
- [3. Separar PDF por Capítulos](#3-separar-pdf-por-capítulos)
  - [Descrição](#descrição-2)
  - [Pré-requisitos](#pré-requisitos-2)
  - [Como Usar](#como-usar-2)

## Pré-requisitos Gerais

- **Python 3.x**: Todos os scripts foram desenvolvidos em Python. Se você não o tiver instalado, pode baixá-lo em [python.org](https://www.python.org/downloads/).
- **pip**: O gerenciador de pacotes do Python, que geralmente já vem instalado com o Python.

---

## 1. Comprimir PDF

### Descrição

Este script utiliza o Ghostscript para reduzir o tamanho de um arquivo PDF. É ideal para otimizar PDFs para envio por e-mail ou para publicação na web.

### Pré-requisitos

- **Ghostscript**: Uma ferramenta externa essencial para o funcionamento do script.
  1.  Faça o download no [site oficial do Ghostscript](https://www.ghostscript.com/releases/gsdnld.html).
  2.  Instale o programa em seu computador.
  3.  Após a instalação, localize o caminho para o executável. Em sistemas Windows, geralmente é algo como:
      `C:\Program Files\gs\gs10.03.1\bin\gswin64c.exe`

### Como Usar

1.  **Abra o script** (`comprimir_pdf.py`) em um editor de texto.

2.  **Configure o caminho do Ghostscript**: Na linha `gs_path`, substitua `"definir o caminho do Ghostgenius"` pelo caminho completo do executável que você localizou no passo anterior. Lembre-se de manter o `r` antes das aspas para evitar problemas com as barras invertidas no Windows.

    ```python
    # Exemplo para Windows
    gs_path = r"C:\Program Files\gs\gs10.03.1\bin\gswin64c.exe"
    ```

3.  **Defina os arquivos**:
    - `input_pdf`: Coloque o nome do seu arquivo de entrada. Por padrão, é `"entrada.pdf"`.
    - `output_pdf`: Defina o nome do arquivo comprimido que será gerado.

4.  **Escolha o nível de compressão** (opcional):
    - A linha `-dPDFSETTINGS=/ebook` define a qualidade. Você pode alterar para:
      - `/screen`: Menor qualidade e menor tamanho (ótimo para visualização em tela).
      - `/ebook`: Qualidade média, bom equilíbrio (padrão no script).
      - `/printer`: Alta qualidade, para impressão.
      - `/prepress`: Qualidade máxima, para impressão profissional.

5.  **Execute o script**: Salve o arquivo e, no terminal, navegue até a pasta onde ele está e execute o comando:
    ```bash
    python comprimir_pdf.py
    ```
    O arquivo `saida_comprimida.pdf` será criado na mesma pasta.

---

## 2. Converter DOCX para PDF

### Descrição

Este script abre uma interface gráfica para que você selecione uma pasta de entrada (com arquivos `.docx`) e uma pasta de saída, convertendo todos os documentos para o formato `.pdf`.

### Pré-requisitos

1.  **Biblioteca `docx2pdf`**: Instale a biblioteca necessária através do pip.
    ```bash
    pip install docx2pdf
    ```
2.  **Microsoft Word (para Windows) ou Pages (para macOS)**: A biblioteca `docx2pdf` utiliza o software de edição de texto instalado no seu sistema para realizar a conversão. Portanto, é **obrigatório** ter o Microsoft Word (em sistemas Windows) ou o Pages (em macOS) instalado.

### Como Usar

1.  **Não é necessário editar o script** para o uso básico.

2.  **Execute o script** a partir do terminal:
    ```bash
    python converter_docx_para_pdf.py
    ```
3.  **Selecione a pasta de entrada**: Uma janela do explorador de arquivos será aberta. Navegue e selecione a pasta que contém todos os arquivos `.docx` que você deseja converter.

4.  **Selecione a pasta de saída**: Uma segunda janela será aberta. Navegue e selecione a pasta onde os novos arquivos `.pdf` deverão ser salvos.

5.  **Aguarde a conclusão**: Ao final do processo, uma mensagem de sucesso ou de erro será exibida.

---

## 3. Separar PDF por Capítulos

### Descrição

Este script divide um único arquivo PDF em vários arquivos menores, um para cada capítulo. Em seguida, ele agrupa todos os capítulos gerados em um único arquivo `.zip`.

### Pré-requisitos

1.  **Biblioteca `PyPDF2`**: Instale a biblioteca para manipulação de PDFs via pip.
    ```bash
    pip install PyPDF2
    ```

### Como Usar

1.  **Abra o script** (`separar_pdf.py`) em um editor de texto.

2.  **Configure o arquivo de entrada**: Na linha `pdf_path`, altere `"exemplo.pdf"` para o nome do seu arquivo PDF.
    ```python
    pdf_path = "meu_documento_completo.pdf"
    ```

3.  **Defina os capítulos**: A parte mais importante é configurar a lista `chapters`.
    - Cada item na lista é uma tupla no formato `("Nome do Capítulo", pagina_inicial)`.
    - `pagina_inicial`: **Importante!** O número da página aqui deve ser o **número que você vê no seu leitor de PDF menos 1**. Por exemplo, se um capítulo começa na página **6** do leitor, você deve inserir o número **5** no script.

    **Exemplo de configuração:**
    ```python
    # Supondo que o PDF tenha a seguinte estrutura:
    # - Introdução: começa na página 3
    # - Desenvolvimento: começa na página 15
    # - Conclusão: começa na página 40
    
    chapters = [
        ("Introdução", 2),      # Página 3 - 1 = 2
        ("Desenvolvimento", 14), # Página 15 - 1 = 14
        ("Conclusão", 39),     # Página 40 - 1 = 39
    ]
    ```
    O script calcula automaticamente a página final de cada capítulo.

4.  **Execute o script**: Salve suas alterações e execute o comando no terminal:
    ```bash
    python separar_pdf.py
    ```

5.  **Verifique os resultados**:
    - Uma nova pasta chamada `capitulos_pdf` será criada, contendo os PDFs de cada capítulo.
    - Um arquivo `exemplo.zip` (ou o nome que você definiu na variável `zip_filename`) será criado com todos os capítulos compactados.
