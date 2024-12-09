# Capstone-Individual-Implementation
Individual Implementation Portion of Early Implementation Deliverable for Snow Leopard Team

## Aspect of Project 1: Profile Scraper
### How to Run:
1. Open scraper folder in VS Code
2. In terminal, install pdfplumber `pip install pdfplumber`
3. In terminal, confirm installation `pip show pdfplumber`
4. In terminal, install pymupdf `pip install pymupdf`
5. In terminal, confirm installation `pip show pymupdf`
6. Run pdf.scraper.py, enter "profile.pdf" in terminal when directed to "Enter the path to the PDF file:"

---

## Aspect of Project 2: HTML for Profile Creation View
### How to Run: (2 Options)

#### Web Browser
1. Save the `.html` file.
2. Locate the file in the file explorer.
3. Right-click on the file, click "Open With," and select your preferred browser.

#### Code Editor (VS Code)
1. Ensure you have installed the "Live Server" extension from the VS Code Extension Marketplace.
2. Open the `.html` file in VS Code.
3. Right-click on the file and select "Open with Live Server."

---

## Summary

### Description:
My first implementation was the PDF scraper, which extracts text from a PDF file provided by the user. It checks if the file exists, reads the text from each page, and saves it in a text file. The scraper is simple to use and processes each page to handle large files easily. The second implementation was the profile form, which is designed to collect user information, including personal details, executive summary, expertise, and certifications, in a clean and easy-to-use format. The "Add Project" button lets users add more project experience fields dynamically by duplicating and clearing existing fields. This allows users to input multiple experiences seamlessly while keeping the form organized and functional. 

### Challenges & Solutions:
#### Profile Scraper
- **Challenge:** Checking if the file exists before processing is necessary to avoid runtime errors if the user provides an incorrect file path.
- **Solution:** Use os.path.exists() to verify the file's existence and display an error message if the file is not found.

#### HTML for Profile Creation View
- **Challenge:** When the "Add Project" button is clicked, the duplicated fields have the same IDs as the original fields, which can cause issues with form validation or JavaScript.
- **Solution:** Remove or update the IDs in the duplicated fields to ensure they are unique. For example, we could remove the IDs entirely or add a unique number to them when duplicating the fields.

---

## Next Steps:
### Profile Scraper
- Create a schema for the database.
- Create an API that can take the scraped information and store it within the database correctly.

### HTML for Profile Creation View
- Use React to style the `.html` file, including:
  - A header with the Cognizant name and logo at the top.
- Convert the HTML to JSX to be usable with React (have not learned React or JSX yet, but decided to implement in HTML because research said it would be easy to convert into a JSX file)
