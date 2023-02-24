from abc import ABC, abstractmethod


class FileProcessor(ABC):
    def __init__(self):
        self._file = None

    def _generate_text_string(self):
        text_string = '\n'.join(self._extract_content())
        return text_string

    @abstractmethod
    def _extract_content(self):
        pass

    @abstractmethod
    def _read_file(self):
        pass

    @abstractmethod
    def get_file(self):
        pass

