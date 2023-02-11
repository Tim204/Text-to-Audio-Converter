from converters.pdf_to_audio import PDFtoTextConverter
from converters.string_to_audio import StringToAudioConverter


def converter_app():
    converters = [StringToAudioConverter(), PDFtoTextConverter()]
    for converter in converters:
        converter.convert_file()


converter_app()