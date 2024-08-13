import aspose.pdf as ap

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def pdfmaker(filename, paragraph):
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment(paragraph)

    page.paragraphs.add(text_fragment)

    document.save(
        'C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mypdffiles/' + filename + '.pdf')  # Save updated PDF
    print(
        f'----------------------------------------------------pdf{filename}.pdf created succesefully---------------------------------------------')


def pdfmaker_2(filename, paragraph):
    output_file = "output.pdf"
    c = canvas.Canvas(
        'C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mypdffiles/' + filename + '.pdf',
        pagesize=letter)
    font_size = 10
    c.setFont("Helvetica", font_size)
    c.drawString(100, 500, paragraph)
    c.save()
    print(f"PDF created and saved as '{output_file}'")
