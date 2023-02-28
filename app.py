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

# chars = ["o", "o"]
# word = "Hello"
# has_all = "my space" if any([char not in word for char in chars]) else "all lies"
# chars = ["a"]
# word = "Hello"
# has_all = "valid" if not any([char in word for char in chars]) else "not valid"
# print(has_all)

