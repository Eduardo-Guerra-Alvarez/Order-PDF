from pypdf import PdfReader

file = '/data/data/com.termux/files/home/storage/downloads/TCS030402UB7_2460099_2024-11-26.pdf'
reader = PdfReader(file)

print(f'Number Page: {len(reader.pages)}')

page = reader.pages[0]

#text = page.extract_text(extraction_mode="layout", layout_mode_strip_rotated=False)
#text = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
#text = page.extract_text(extraction_mode="layout", layout_mode_scale_weight=1.0)
text = page.extract_text()
split_text = text.split('\n')
for txt in split_text:
    if('Periodo de pago' in txt):
        print(txt.split(' ')[-1])
