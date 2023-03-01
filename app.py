from converters.docx_to_audio import DocxToAudioConverter
from converters.pdf_to_audio import PDFtoTextConverter
from converters.string_to_audio import StringToAudioConverter


class ConverterApp:
    def __init__(self, conversion_type):
        self._ct = conversion_type

    def convert(self):
        self._ct.convert_file()


ca = ConverterApp(DocxToAudioConverter())
ca.convert()

