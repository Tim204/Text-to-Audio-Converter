import PyPDF2


class PDFFileProcessor:
    """A PDF processing class"""
    def __init__(self, pdf_file):
        self._pdf_file = pdf_file

    def generate_text_string(self):
        text_string = " ".join(self._extract_content())
        return text_string

    def _open_pdf(self):
        return open(self._pdf_file, "rb")

    def _read_pdf(self):
        pdf_reader = PyPDF2.PdfReader(self._open_pdf())
        return pdf_reader

    def _extract_content(self):
        content_list = []
        page_count = len(self._read_pdf().pages)
        for page_number in range(page_count):
            page = self._read_pdf().pages[page_number]
            content_list.append(page.extract_text())
        return content_list

