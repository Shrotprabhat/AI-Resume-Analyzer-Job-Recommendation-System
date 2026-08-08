from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_docx(uploaded_file):
    doc = Document(uploaded_file)
    text = ""

    for para in doc.paragraphs:
        if para.text.strip():
            text += para.text + "\n"

    return text


def extract_resume_text(uploaded_file):
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif filename.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    else:
        raise ValueError("Unsupported File Format")