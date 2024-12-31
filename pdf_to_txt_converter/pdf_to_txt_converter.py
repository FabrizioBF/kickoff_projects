import PyPDF2
import os

if not os.path.isdir("temp"):
    os.mkdir("temp")

# Solicita o caminho do PDF e do TXT
pdfpath = input("Insira o caminho do arquivo PDF: ")
txtpath = input("Insira o caminho do arquivo TXT de saída (ou deixe vazio): ")

# Diretório base para arquivos de texto
BASEDIR = os.path.realpath("temp")

if len(txtpath.strip()) == 0:
    txtpath = os.path.join(BASEDIR, os.path.basename(
        pdfpath).replace(".pdf", ".txt"))

try:
    with open(pdfpath, 'rb') as pdfobj:
        # Para versões mais recentes do PyPDF2
        pdfread = PyPDF2.PdfReader(pdfobj)
        x = len(pdfread.pages)
        for i in range(x):
            pageObj = pdfread.pages[i]
            with open(txtpath, 'a+', encoding='utf-8') as f:
                f.write(pageObj.extract_text())
            print(pageObj.extract_text())
except Exception as e:
    print(f"Erro: {e}")
