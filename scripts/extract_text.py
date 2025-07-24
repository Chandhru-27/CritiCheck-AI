from pypdf import PdfReader

def extract_test_from_pdf(pdf_path : str) -> str:
    text = ""
    try: 
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        raise ValueError(f"PDF extraction failed: {str(e)}")

    return text.strip()


if __name__ == "__main__":
    text = extract_test_from_pdf(r"C:\Dev\project_mmbu\sample_pdf.pdf")
    print(text)
