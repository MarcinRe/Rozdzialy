# -*- coding: utf-8 -*-
print"---------------6.12-----------------"
import sys
print '\n'.join(sys.modules.keys())
print"---------------6.13-----------------"
import fileinfo
print '\n'.join(sys.modules.keys())
print"---------------6.14-----------------"
from fileinfo import MP3FileInfo
print MP3FileInfo.__module__
print sys.modules[MP3FileInfo.__module__]
