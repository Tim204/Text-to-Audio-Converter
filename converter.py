import os
from abc import ABC, abstractmethod
from gtts import gTTS


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
        self._string = ""
        self._language = self._DEFAULT_LANGUAGE
        self._filename = ""

    def convert(self):
        print("Converting String to Audio...")
        self.set_str_obj()
        self.set_filename()
        converted = gTTS(self._string, lang=self._language, slow=False)
        converted.save(self._filename)
        self.play()

    def set_language(self, language):
        self._language = language
        return language

    def set_str_obj(self):
        if self._string is not None:
            self._string = input("Enter your string here: ")
        return self._string

    def set_filename(self):
        if self._filename is not None:
            self._filename = input(f"File name: ")
        return self._filename

    def play(self):
        os.system(self._filename + ".mp3")


def converter_app():
    converters = [StringToAudioConverter()]
    for converter in converters:
        converter.convert()


converter_app()