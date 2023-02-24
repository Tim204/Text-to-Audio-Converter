from tkinter import filedialog as fd
from converters.converter import Converter
from file_processors.docx_processor import DocxFileProcessor


class DocxToAudioConverter(Converter):

    def __init__(self):
        super().__init__()
        self._file_types = (
            ("pdf files", "*.docx"),
        )

    def convert_file(self):
        print("Converting docx to audio...")
        self._start_conversion()

    def _set_str_obj(self):
        processor = DocxFileProcessor(fd.askopenfilename(filetypes=self._file_types))
        self._string_obj = processor.get_text_string()
        return self._string_obj

    def __str__(self):
        return "Word document to audio"


wd = DocxToAudioConverter()
wd.convert_file()

