from converters.converter import Converter


class StringToAudioConverter(Converter):
    def __init__(self):
        super().__init__()

    def convert_file(self):
        self._start_conversion()

    def _set_str_obj(self):
        while self._string_obj == "":
            self._string_obj = input("Enter your text here: ")
        return self._string_obj

    def __str__(self):
        return "Text sting to audio"

