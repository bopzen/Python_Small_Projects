import fitz  # PyMuPDF


def convert_pdf_to_image(pdf_path, output_image_path, page_number=0, resolution=300):
    pdf_document = fitz.open(pdf_path)
    pdf_page = pdf_document[page_number]

    # Create a Pix object (an image) from the PDF page
    pix = pdf_page.get_pixmap(matrix=fitz.Matrix(resolution / 72.0, resolution / 72.0))

    # Save the Pix object as an image file
    pix.save(output_image_path)


convert_pdf_to_image("your_pdf_name.pdf", "your_png_name.png", page_number=0, resolution=300)