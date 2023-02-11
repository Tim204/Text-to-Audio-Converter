from converters.converter import Converter


class StringToAudioConverter(Converter):
    def __init__(self):
        super().__init__()

    def convert_file(self):
        print("Converting String to Audio...")
        self._start_conversion()

    def _set_str_obj(self):
        if self._string_obj is not None:
            self._string_obj = input("Enter your string here: ")
        return self._string_obj
