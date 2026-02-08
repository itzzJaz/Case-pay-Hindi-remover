# install first if needed:
# pip install pypdf

from pypdf import PdfReader, PdfWriter

def remove_alternate_pages(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Loop through pages
    for i in range(len(reader.pages)):
        # Keep page 1,3,5... (index 0,2,4...)
        if i % 2 == 0:
            writer.add_page(reader.pages[i])

    # Save new PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

remove_alternate_pages("2-1-1 English L & L.pdf", "output.pdf")