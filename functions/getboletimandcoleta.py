import PyPDF2
import re

def get_boletim_and_coleta(pdf_path):
    # Abre o arquivo PDF
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        # Extrai texto de cada página
        all_text = ""
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            all_text += page.extract_text()

    # print("Texto Extraído do PDF:")
    # print(all_text)

    # Captura: Preços 52/202 4
    # Grupo: 52
    # Ancoramos com o "Preços" para não buscar outra data
    numero_boletim_pattern = r"Preços\s+(\d+)\/\d{3}\s\d{1}"
    numero_boletim_match = re.search(numero_boletim_pattern, all_text)
    # Captura: Minor Harada” em 17/07/202 4
    # Grupo: 17/07/202 4
    # Ancoramos com Minor Harada para não buscar outra data
    data_coleta_pattern = r"Minor Harada[^\d]*(\d{2}\/\d{2}\/\d{3}\s\d{1})"
    data_coleta_match = re.search(data_coleta_pattern, all_text)

    numero_boletim = numero_boletim_match.group(1) if data_coleta_match else "Não encontrado"
    data_coleta = data_coleta_match.group(1).replace(' ','') if data_coleta_match else "Não encontrado"
    print(f'Identificado numero do boletim: {numero_boletim} | Data de coleta {data_coleta}')
    
    return numero_boletim, data_coleta

