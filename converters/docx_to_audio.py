from converters.converter import Converter
from file_processors.docx_processor import DocxFileProcessor


class DocxToAudioConverter(Converter):

    def __init__(self):
        super().__init__()
        self._processor = DocxFileProcessor()

    def convert_file(self):
        self._start_conversion()

    def _set_str_obj(self):
        if self._string_obj == "":
            self._processor.get_file()
            try:
                self._string_obj = self._processor.get_text_string()
            except:
                print("\nOperation Cancelled")
                exit()
        return self._string_obj

    def set_filename(self):
        self._filename = self._processor.get_file_name().replace(" ", "_")
        return self._filename

    def __str__(self):
        return "Word document to audio"



