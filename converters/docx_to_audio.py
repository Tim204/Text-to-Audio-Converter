from converters.converter import Converter
from file_processors.docx_processor import DocxFileProcessor


class DocxToAudioConverter(Converter):

    def __init__(self):
        super().__init__()

    def convert_file(self):
        self._start_conversion()

    def _set_str_obj(self):
        if self._string_obj == "":
            processor = DocxFileProcessor()
            processor.get_file()
            try:
                self._string_obj = processor.get_text_string()
            except:
                print("No valid file provided")
                exit()
        return self._string_obj

    def __str__(self):
        return "Word document to audio."



