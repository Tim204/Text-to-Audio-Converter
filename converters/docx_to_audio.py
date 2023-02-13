from tkinter import filedialog as fd
from converters.converter import Converter
from converters.file_processors import DocxFileProcessor


class DocxToAudioConverter(Converter):

    def __init__(self):
        super().__init__()

    def convert_file(self):
        print("Converting docx to audio...")
        self._start_conversion()

    def _set_str_obj(self):
        processor = DocxFileProcessor(fd.askopenfilename())
        self._string_obj = processor.generate_text_string()
        return self._string_obj


dox = DocxToAudioConverter()
dox.convert_file()
