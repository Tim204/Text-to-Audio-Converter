from abc import ABC, abstractmethod
from network_status.connectivity_cheker import ConnectivityChecker
from gtts import gTTS
import os


class Converter(ABC):
    _DEFAULT_LANGUAGE = "en"
    _network_status = ConnectivityChecker()
    _file_format = ".mp3"

    def __init__(self):
        self._string_obj = ""
        self._language = self._DEFAULT_LANGUAGE
        self._filename = ""
        self._audio_file = None

    def _start_conversion(self):
        print(f"Converting {self.__class__.__str__(self)}")
        self._set_str_obj()
        self.set_filename()
        self._convert(self._string_obj)
        self.save_file(self._audio_file)
        self.play(self._filename)

    def _convert(self, str_object):
        if self._network_status.is_connected():
            print(f"\nConverting '{self._filename}' to audio...")
            self._audio_file = gTTS(str_object, lang=self._language, slow=False)
        else:
            exit(f"Unable to convert {self.__class__.__str__(self)}."
                 f"\nYou need to connect to the internet in order to perform the conversion")

    def set_language(self, language):
        self._language = language
        return language

    @abstractmethod
    def _set_str_obj(self):
        pass

    def save_file(self, audio_file):
        if self._filename != "":
            self._audio_file = audio_file.save(self._filename + self._file_format)
            print(f"\n{self._filename} successfully converted!")

    def set_filename(self):
        while self._filename == "":
            try:
                self._filename = input("Define a filename: ").replace(" ", "_")
            except:
                print("Names cannot contain any of the following characters:\n\ / : * ? ' < > |" )
        return self._filename

    def play(self, filename):
        os.system(filename + self._file_format)
