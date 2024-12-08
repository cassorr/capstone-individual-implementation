import pdfplumber  # library used to extract text from PDF files
import fitz  # PyMuPDF library used to extract images and other content from PDFs (might be needed in the future with cert badges)
import os  # library for interacting with the file system

def scrape_pdf_text(file_path):
    extracted_text = {}  # dictionary to store text for each page
    with pdfplumber.open(file_path) as pdf:  # open the PDF file
        for i, page in enumerate(pdf.pages):  # loop through all pages in the PDF
            # extract text from the current page and save it to the dictionary
            extracted_text[f"Page {i + 1}"] = page.extract_text()
    return extracted_text  # return the dictionary with extracted text

def main():
    # ask the user to enter the path to the PDF file they want to scrape
    file_path = input("Enter the path to the PDF file: ").strip()

    # check if the file exists at the given path
    if not os.path.exists(file_path):  
        print(f"Error: File '{file_path}' not found.")  
        return  

    # extract text from the PDF
    print("Extracting text...")  # inform user that text extraction is starting
    text_data = scrape_pdf_text(file_path)  # call the text extraction function

    # save the extracted text to a file
    text_output_path = "extracted_text.txt"  # file to save the extracted text
    with open(text_output_path, "w", encoding="utf-8") as text_file:  # open the file 
        for page, content in text_data.items():  # loop through each page's text
            # write the page number and its text to the file
            text_file.write(f"{page}:\n{content}\n\n")
    print(f"Text extracted and saved to {text_output_path}.")  # inform the user where text is saved

if __name__ == "__main__":
    main()  # Call the main function to start the program
