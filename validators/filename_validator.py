
class FilenameValidator:
    def __init__(self):
        self._special_chars = ("?", "/", ":", "~")
        self._valid = True

    def is_valid(self, filename):
        self._valid = True if not any([chars in self._special_chars for chars in filename]) else False
        return self._valid

    def get_special_chars(self):
        return str(self._special_chars).strip("()")


