from converters.converter import Converter
from converters.pdf_processor import PDFFileProcessor
from gtts import gTTS


class PDFtoTextConverter(Converter):

    def __init__(self):
        super().__init__()

    def convert(self):
        print("Converting PDF to Audio...")
        self._set_str_obj()
        self.set_filename()
        converted = gTTS(self._string_obj, lang=self._language, slow=False)
        converted.save(self._filename + ".mp3")
        self.play()

    def _set_str_obj(self):
        processor = PDFFileProcessor("Release Form.pdf")
        self._string_obj = processor.generate_text_string()
        return self._string_obj


c = PDFtoTextConverter()
c.convert()
