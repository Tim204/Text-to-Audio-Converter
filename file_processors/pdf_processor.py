from file_processors.processors_interface import FileProcessor
from tkinter import filedialog as fd
import PyPDF2


class PDFFileProcessor(FileProcessor):

    def __init__(self):
        super().__init__()
        self._file_types = (
            ("pdf files", "*.pdf"),
        )

    def get_text_string(self):
        return self._generate_text_string()

    def _open_pdf(self):
        return open(self._file, "rb")

    def _extract_content(self):
        content_list = []
        page_count = len(self._read_file().pages)
        for page_number in range(page_count):
            page = self._read_file().pages[page_number]
            content_list.append(page.extract_text())
        return content_list

    def _read_file(self):
        pdf_reader = PyPDF2.PdfReader(self._open_pdf())
        return pdf_reader

    def get_file(self):
        self._file = fd.askopenfilename(filetypes=self._file_types)
        return self._file


