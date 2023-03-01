from converters.converter import Converter
from validators.filename_validator import FilenameValidator


class StringToAudioConverter(Converter):
    def __init__(self):
        super().__init__()

    def convert_file(self):
        self._start_conversion()

    def _set_str_obj(self):
        while self._string_obj == "":
            self._string_obj = input("Enter your text here: ")
        return self._string_obj

    def set_filename(self):
        validator = FilenameValidator()
        while self._filename == "":
            mp3_filename = input("Define a filename: ").replace(" ", "_")
            if validator.validate_filename(mp3_filename):
                self._filename = mp3_filename
            else:
                print(f"Filenames should not contain any of the following characters: {validator.get_special_chars()}\n")
                self._filename = ""
        return self._filename

    def __str__(self):
        return "Text sting to audio"

