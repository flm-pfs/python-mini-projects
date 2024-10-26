import os
from PyPDF2 import PdfMerger


def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()

    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            # Append each PDF file to the merger object
            merger.append(pdf_file)
        else:
            print(f"File {pdf_file} does not exist.")

    merger.write(output_path)  # Write the merged PDF to the output path
    merger.close()  # Close the merger object
    print(f"Merged PDF saved to {output_path}")


if __name__ == "__main__":
    pdf_files = [
        "PDFMerger/file1.pdf",
        "PDFMerger/file2.pdf",
    ]
    output_path = "PDFMerger/merged_output.pdf"
    # Call the merge_pdfs function with the given PDF files and output path
    merge_pdfs(pdf_files, output_path)
