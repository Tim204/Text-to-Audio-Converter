from converters.file_processors.processors_interface import FileProcessor
import docx


class DocxFileProcessor(FileProcessor):

    def __init__(self, file):
        super().__init__(file)

    def get_test_string(self):
        return self._generate_text_string()

    def _extract_content(self):
        content_list = []
        for paragraph in self._read_file().paragraphs:
            content_list.append(paragraph.text)
        return content_list

    def _read_file(self):
        docx_reader = docx.Document(self._file)
        return docx_reader
