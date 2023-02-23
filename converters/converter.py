from abc import ABC, abstractmethod
from network_status.connectivity_cheker import ConnectivityChecker
from gtts import gTTS
import os


class Converter(ABC):
    _DEFAULT_LANGUAGE = "en"
    _NETWORK_CONNECTION = ConnectivityChecker()

    def __init__(self):
        self._string_obj = ""
        self._language = self._DEFAULT_LANGUAGE
        self._filename = ""
        self._converted_file = None

    def _start_conversion(self):
        self._set_str_obj()
        self.set_filename()
        self.convert(self._string_obj)
        self.save_file(self._converted_file)
        self.play(self._converted_file)

    def convert(self, str_object):
        if self._NETWORK_CONNECTION.is_connected():
            self._converted_file = gTTS(str_object, lang=self._language, slow=False)
        else:
            print("Please ensure that you are connected to the internet")

    def set_language(self, language):
        self._language = language
        return language

    @abstractmethod
    def _set_str_obj(self):
        pass

    def save_file(self, converted_file):
        if self._filename != "":
            converted_file.save(self._filename)

    def set_filename(self):
        while self._filename == "":
            self._filename = input(f"File name: ").replace(" ", "_")
        return self._filename

    def play(self, filename):
        os.system(filename)
