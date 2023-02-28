

class FilenameValidator:
    def __init__(self):
        self._special_chars = ["?", "/", ":", "~"]

    def is_valid(self, filename):
        valid = True if not any([chars in self._special_chars for chars in filename]) else False
        return valid


fv = FilenameValidator()
print(fv.is_valid("alured~"))