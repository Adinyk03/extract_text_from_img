import PyPDF2
from PIL import Image
import pytesseract
import io

pdf_file_path = '/Users/adi/Desktop/image pdf.pdf'

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]

        images = []
        try:
            resources = page['/Resources']
        except KeyError:
            continue

        xObject = resources.get('/XObject')
        if xObject:
            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    images.append(xObject[obj])

        # Perform OCR on each image
        for image in images:
            size = (image['/Width'], image['/Height'])
            data = image.get_data()

            if image['/Filter'] == '/FlateDecode':
                img = Image.frombytes('RGB', size, data)
            else:
                img = Image.open(io.BytesIO(data))

            extracted_text = pytesseract.image_to_string(img)


            print(f"Extracted text from Page {page_num + 1}, Image {image}:")
            print(extracted_text)
