from pypdf import PdfReader
import os

def find_pdfs(path):
    # create a list to store the PDF files
    pdf_files = []
    # loop through the directory and find all PDF files
    for filename in os.listdir(path):
        if filename.endswith('.pdf'):
            pdf_files.append(filename)
            
    return pdf_files

def orderPDFFiles(path):
    list_of_files = []
    if os.path.exists(path):
        get_pdfs = find_pdfs(path)
        for file_name in get_pdfs:
            new_file_name = getDateName(file_name)
            if (new_file_name in list_of_files):
                os.rename(f'./{file_name}', f'./{new_file_name}_2.pdf')
            else :
                os.rename(f'./{file_name}', f'./{new_file_name}.pdf')
            list_of_files.append(new_file_name)


def getDateName(file_name):
    reader = PdfReader(file_name)
    page = reader.pages[0]

    #text = page.extract_text(extraction_mode="layout", layout_mode_strip_rotated=False)
    #text = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
    #text = page.extract_text(extraction_mode="layout", layout_mode_scale_weight=1.0)
    text = page.extract_text()
    split_text = text.split('\n')
    format_date = ''
    for txt in split_text:
        if('Periodo de pago' in txt):
            date = txt.split(' ')[-1]
            format_date = date.split('/')
            
    return format_date[0] + "-" + format_date[1] + "-" + format_date[2]

        
orderPDFFiles('./')