---

# Extract Text from Image in PDF

This repository contains a Python script that facilitates text extraction from images embedded in a PDF file. The script utilizes libraries such as PyPDF2, PIL (Python Imaging Library), and Tesseract OCR for efficient image processing and text extraction.

## Features

- Extracts text from image-based PDF documents.
- Utilizes PyPDF2 to read PDF files and identify images within them.
- Uses PIL to handle image data, converting it to a readable format for Tesseract OCR.
- Leverages Tesseract OCR to perform Optical Character Recognition on images.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Adinyk03/extract_text_from_img.git
    ```

2. Install the required Python libraries:

    ```bash
    pip install PyPDF2 pillow pytesseract
    ```

3. Ensure Tesseract OCR is installed on your system. You can download it from: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## Usage

1. Place your PDF file containing images in the repository directory.
2. Modify the `pdf_file_path` variable in the Python script to match your PDF file's path.
3. Run the Python script:

    ```bash
    python extract_text_from_pdf.py
    ```

4. The script will process the PDF, extract images, perform OCR, and display the extracted text from each image.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
