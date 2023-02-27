from file_processors.processors_interface import FileProcessor
from tkinter import filedialog as fd
import docx
import os


class DocxFileProcessor(FileProcessor):

    def __init__(self):
        super().__init__()
        self._file_types = (
            ("MS Word files", "*.docx"),
        )

    def get_text_string(self):
        return self._generate_text_string()

    def _extract_content(self):
        content_list = []
        for paragraph in self._read_file().paragraphs:
            content_list.append(paragraph.text)
        return content_list

    def _read_file(self):
        docx_reader = docx.Document(self._file)
        return docx_reader

    def get_file(self):
        self._file = fd.askopenfilename(filetypes=self._file_types)
        return self._file

    def get_file_name(self):
        file_name = os.path.basename(self._file)
        return os.path.splitext(file_name)[0]

