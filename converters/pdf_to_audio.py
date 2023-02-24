from converters.converter import Converter
from file_processors.pdf_processor import PDFFileProcessor
from tkinter import filedialog as fd


class PDFtoTextConverter(Converter):

    def __init__(self):
        super().__init__()
        self._file_types = (
            ("pdf files", "*.pdf"),
        )

    def convert_file(self):
        print("Converting PDF to Audio...")
        self._start_conversion()

    def _set_str_obj(self):
        if self._string_obj == "":
            processor = PDFFileProcessor(fd.askopenfilename(filetypes=self._file_types))
            try:
                self._string_obj = processor.get_text_string()
            except FileNotFoundError:
                print("No valid file provided")
                exit()
            return self._string_obj

    def __str__(self):
        return "PDF file to audio"


c = PDFtoTextConverter()
c.convert_file()