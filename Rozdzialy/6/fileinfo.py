# -*- coding: utf-8 -*-
import os
import sys
from UserDict import UserDict


def stripnulls(data):
    u"usuwa białe znaki i nulle"
    return data.replace("\00", " ").strip()


class FileInfo(UserDict):
    u"przechowuje metadane pliku"

    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["plik"] = filename


class MP3FileInfo(FileInfo):
    u"przechowuje znaczniki ID3v1.0 MP3"
    tagDataMap = {"title": (3, 33, stripnulls),
                  "artist": (33, 63, stripnulls),
                  "album": (63, 93, stripnulls),
                  "year": (93, 97, stripnulls),
                  "comment": (97, 126, stripnulls),
                  "genre": (127, 128, ord)}

    def __parse(self, filename):
        u"parsuje znaczniki ID3v1.0 z pliku MP3"
        self.clear()
        try:
            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-128, 2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()
            if tagdata[:3] == 'TAG':
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])
        except IOError:
            pass

    def __setitem__(self, key, item):
        if key == "plik" and item:
            self.__parse(item)
        FileInfo.__setitem__(self, key, item)


def listDirectory(directory, fileExtList):
    u"zwraca listę obiektów zawierających metadane dla plików o podanych rozszerzeniach"
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f) for f in fileList \
                if os.path.splitext(f)[1] in fileExtList]

    def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
        u"zwraca klasę metadanych pliku na podstawie podanego rozszerzenia"
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo

    return [getFileInfoClass(f)(f) for f in fileList]


if __name__ == "__main__":
    for info in listDirectory("/music/_singles/", [".mp3"]):
        print "\n".join(["%s=%s" % (k, v) for k, v in info.items()])
        print