print"---------------5.5-6---------------"
class FileInfo(dict):
    u"przechowuje metadane pliku"
    def __init__(self,filename=None):
        dict.__init__(self)
        self["plik"]=filename
print"---------------5.7---------------"
#import fileinfo
f=FileInfo("/music/_singles/kairo.mp3")
print f.__class__
print f.__doc__
print f
print"---------------5.8---------------"
def leakmem():
    f=FileInfo("/music/_singles/kairo.mp3")

for i in range(100):
    leakmem()
