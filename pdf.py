from pypdf import PdfReader

def read_pdf(user_profile):
    pdf=PdfReader(user_profile)
    #save the information in raw text
    raw_text = ''
    for i, page in enumerate(pdf.pages):
        content = page.extract_text()
        if content:
            raw_text+=content
    return(raw_text)
    