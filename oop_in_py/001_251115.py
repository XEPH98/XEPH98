import abc

class MediaLoader(abc.ABC): #abc.ABC introduces a metaclass (a class used to build the concrete class definitions).
    @abc.abstractmethod
    def play(self) -> None:
        pass
    @property
    @abc.abstractmethod
    def ext(self) -> str:
        pass
class Wav(MediaLoader):
    pass

#x = Wav() #this line will trow TypeError

class Ogg(MediaLoader):
    ext = ".ogg"
    def play(self):
        pass
o = Ogg()