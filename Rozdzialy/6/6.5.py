# -*- coding: utf-8 -*-
print"---------------5.12---------------"
import fileinfo
f=fileinfo.FileInfo("C:\Users\Public\Music\Sample Music\Kalimba.mp3")
print f
print f.__getitem__("plik")
print f["plik"]
print"---------------5.13---------------"
f.__setitem__("gatunek",31)
print f
f["gatunek"]=32
print f
print"---------------5.15---------------"
import fileinfo
mp3file = fileinfo.MP3FileInfo()
print mp3file
mp3file["plik"]="C:\Users\Public\Music\Sample Music\Kalimba.mp3"
print mp3file
mp3file["plik"]="C:\Users\Public\Music\Sample Music\Sleep Away.mp3"
print mp3file

