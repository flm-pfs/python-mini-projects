import PyPDF2
import pyttsx3


def read_pdf_aloud(file_path):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Open the PDF file in read-binary mode
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Check if the PDF file is encrypted
        if pdf_reader.is_encrypted:
            print("The PDF file is encrypted.")
            return

        # Get the number of pages in the PDF document
        num_pages = len(pdf_reader.pages)

        # Iterate through each page and extract text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            print(f"Page {page_num + 1}:\n")
            print(text)
            print("\n" + "="*80 + "\n")
            engine.say(text)
            engine.runAndWait()


# Example usage
file_path = 'PDFReader\example.pdf'
read_pdf_aloud(file_path)
