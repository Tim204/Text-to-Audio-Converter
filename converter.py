import os
from abc import ABC, abstractmethod
from gtts import gTTS
import PyPDF2


class Converter(ABC):

    @abstractmethod
    def convert(self):
        pass

    @abstractmethod
    def save(self, converted_file, file_name):
        pass
    pass


class StringToAudioConverter:
    _DEFAULT_LANGUAGE = "en"

    def __init__(self):
        self._string_obj = ""
        self._language = self._DEFAULT_LANGUAGE
        self._filename = ""

    def convert(self):
        print("Converting String to Audio...")
        self.set_str_obj()
        self.set_filename()
        converted = gTTS(self._string_obj, lang=self._language, slow=False)
        converted.save(self._filename + ".mp3")
        self.play()

    def set_language(self, language):
        self._language = language
        return language

    def set_str_obj(self):
        if self._string_obj is not None:
            self._string_obj = input("Enter your string here: ")
        return self._string_obj

    def set_filename(self):
        if self._filename is not None:
            self._filename = input(f"File name: ")
        return self._filename

    def play(self):
        os.system(self._filename + ".mp3")


class PDFFileProcessor:
    """A PDF processing class"""
    def __init__(self, pdf_file):
        self._pdf_file = pdf_file

    def open_pdf(self):
        return open(self._pdf_file, "rb")

    def read_pdf(self):
        pdf_reader = PyPDF2.PdfReader(self.open_pdf())
        return pdf_reader

    def extract_content(self):
        content_list = []
        page_count = len(self.read_pdf().pages)
        for page_number in range(page_count):
            page = self.read_pdf().pages[page_number]
            content_list.append(page.extract_text())
        return content_list


class PDFtoTextConverter:
    _DEFAULT_LANGUAGE = "en"

    def __init__(self):
        self._string_obj = ""
        self._language = self._DEFAULT_LANGUAGE
        self._filename = ""

    def convert(self):
        pass

    def save(self, converted_file, file_name):
        pass


def converter_app():
    converters = [StringToAudioConverter(), PDFtoTextConverter()]
    for converter in converters:
        converter.convert()


converter_app()