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

    @abstractmethod
    def save(self, converted_file, file_name):
        pass
    pass
