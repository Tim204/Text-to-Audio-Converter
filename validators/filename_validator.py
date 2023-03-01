
class FilenameValidator:
    def __init__(self):
        self._special_chars = ("?", "/", ":", "~")
        self._is_valid = True

    def validate_filename(self, filename):
        self._is_valid = True if not any([chars in self._special_chars for chars in filename]) else False
        return self._is_valid

    def get_special_chars(self):
        return str(self._special_chars).strip("()")


