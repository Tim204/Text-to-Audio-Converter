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

    def _start_conversion(self):
        # if self._NETWORK_CONNECTION.is_connected():
            self._set_str_obj()
            self.set_filename()
            try:
                converted = gTTS(self._string_obj, lang=self._language, slow=False)
                converted.save(self._filename + ".mp3")
                self.play()
            except:
                print("""An error occurred.\n\nMake sure the file or text you provided is not empty
                """)
        # else:
        #     print("No internet connection. \nPlease connect to the internet before proceeding")

    def set_language(self, language):
        self._language = language
        return language

    @abstractmethod
    def _set_str_obj(self):
        pass

    def set_filename(self):
        if self._filename is not None:
            self._filename = input(f"File name: ").replace(" ", "_")
        return self._filename

    def play(self):
        os.system(self._filename + ".mp3")
