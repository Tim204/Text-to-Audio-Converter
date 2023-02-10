from converters.converter import Converter
from gtts import gTTS


class StringToAudioConverter(Converter):
    def __init__(self):
        super().__init__()

    def convert(self):
        print("Converting String to Audio...")
        self._set_str_obj()
        self.set_filename()
        converted = gTTS(self._string_obj, lang=self._language, slow=False)
        converted.save(self._filename + ".mp3")
        self.play()

    def _set_str_obj(self):
        if self._string_obj is not None:
            self._string_obj = input("Enter your string here: ")
        return self._string_obj




