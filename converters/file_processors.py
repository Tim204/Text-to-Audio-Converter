from abc import ABC, abstractmethod
import PyPDF2
import docx


class FileProcessor(ABC):
    def __init__(self, file):
        self._file = file

    @abstractmethod
    def generate_text_string(self):
        pass

    @abstractmethod
    def _extract_content(self):
        pass


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


class DocxFileProcessor:
    def __init__(self, docx_file):
        self._docx_file = docx_file

    def generate_text_string(self):
        text_sting = '\n'.join(self._extract_content())
        return text_sting

    def _extract_content(self):
        content_list = []

        for paragraph in self._read_docx().paragraphs:
            content_list.append(paragraph.text)
            print(content_list)
        return content_list

    def _read_docx(self):
        docx_reader = docx.Document(self._docx_file)
        return docx_reader
