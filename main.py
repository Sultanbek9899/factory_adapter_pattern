from sqlite3 import adapters
from sys import argv


class Format:

    def __init__(self, format_name):
        self.__format_name = format_name

    def get_format(self):
        return self.__format_name

#AUDIO FORMATS
class AudioMP3(Format):

    def __init__(self):
        super().__init__("MP3")
    
    def decode(self):
        print("Декод в формат MP4")

class AudioWMA(Format):

    def __init__(self):
        super().__init__("WMA")

    def decode(self):
        print("Декод в формат MP4")

class AudioWAV(Format):
    def __init__(self):
        super().__init__("WAV")


#Video Formats
class VideoMP4(Format):
    def __init__(self):
        super().__init__("MP4")

    def decode(self):
        print("Декод в формат MP4")

class VideoMOV(Format):
    def __init__(self):
        super().__init__("MOV")

    def decode(self):
        print("Декод в формат MOV")
    
class VideoFLV(Format):

    def __init__(self):
        super().__init__("FLV")




class Decode():

    def __init__(self, format):
        self.format = format

    def decoding(self):
        try:
            self.format.decode()
        except AttributeError: 
            print("Подключаем адаптер... ")
            adapter=DecodeFormatAdapter(self.format)
            adapter.decode()

class DecodeFormatAdapter():

    def __init__(self, format):
        self.format = format

    def decode(self):
        print(f"Декод в формат {self.format.get_format()}")

formats = {
    "MOV": VideoMOV,
    "MP4": VideoMP4,
    "FLV": VideoFLV,
    "MP3": AudioMP3,
    "WAV": AudioWAV,
    "WMA": AudioWMA,
}
def create_format(formats, name):
    return formats[name]()


if __name__=="__main__":
    if len(argv) == 1: 
        print("Выберите формат:")
        for n,i in enumerate(formats.keys()):
            print(f"{n}) {i}")
        name = input("Напишите название формата: ").upper()
        format = create_format(formats, name)
        decoder = Decode(format)
        decoder.decoding()
    elif len(argv) == 2:
        format_name = argv[1].upper()
        format = create_format(formats, format_name)
        decoder = Decode(format)
        decoder.decoding()