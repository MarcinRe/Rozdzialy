# -*- coding: utf-8 -*-
print"---------------6.16-----------------"
import os
print os.path.join("C:\\Users\\Public\\Music\\Sample Music\\","kalimba.mp3")
print os.path.join("C:\\Users\\Public\\Music\\Sample Music","kalimba.mp3")
print os.path.expanduser("~")
print os.path.join(os.path.expanduser("~"),"Python")
print"---------------6.17-----------------"
print os.path.split("C:\\Users\\Public\\Music\\Sample Music\\kalimba.mp3")
(filepath,filename)=os.path.split("C:\\Users\\Public\\Music\\Sample Music\\kalimba.mp3")
print filepath
print filename
(shortname, extension) = os.path.splitext(filename)
print shortname
print extension
print"---------------6.18-----------------"
print os.listdir("C:\\Users\\Public\\Music\\Sample Music\\")
dirname="C:\\Users\\Public\\Music\\"
print os.listdir(dirname)
print [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]
print [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, f))]
print"---------------6.20-----------------"
print os.listdir("C:\\Users\\Public\\Music\\Sample Music\\")
import glob
print glob.glob("C:\\Users\\Public\\Music\\Sample Music\\*.mp3")
print glob.glob("C:\\Users\\Public\\Music\\Sample Music\\s*.mp3")
print glob.glob("C:\\Users\\Public\\Music\\*\\*.mp3")


