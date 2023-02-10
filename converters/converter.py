import os
from abc import ABC, abstractmethod


class Converter(ABC):
    _DEFAULT_LANGUAGE = "en"

    def __init__(self):
        self._string_obj = ""
        self._language = self._DEFAULT_LANGUAGE
        self._filename = ""

    @abstractmethod
    def convert(self):
        pass

    def set_language(self, language):
        self._language = language
        return language

    @abstractmethod
    def _set_str_obj(self):
        pass

    def set_filename(self):
        if self._filename is not None:
            self._filename = input(f"File name: ")
        return self._filename

    def play(self):
        os.system(self._filename + ".mp3")
