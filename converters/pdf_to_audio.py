from converters.converter import Converter
from converters.pdf_processor import PDFFileProcessor
from tkinter import filedialog as fd


class PDFtoTextConverter(Converter):

    def __init__(self):
        super().__init__()

    def convert_file(self):
        print("Converting PDF to Audio...")
        self._start_conversion()

    def _set_str_obj(self):
        processor = PDFFileProcessor(fd.askopenfilename())
        self._string_obj = processor.generate_text_string()
        return self._string_obj
