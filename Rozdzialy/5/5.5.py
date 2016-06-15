# -*- coding: utf-8 -*-
print"---------------4.12----------------"
li = ["Larry","Curly"]
print li.pop
print getattr(li,"pop")
getattr(li, "append")("Moe")
print li
print getattr({}, "clear")
#print getattr((), "pop")
print"---------------4.12----------------"
import apihelper
print apihelper.info
print getattr(apihelper, "info")
object = apihelper
method = "info"
print getattr(object,method)
print type(getattr(object, method))
import types
print type(getattr(object, method)) == types.FunctionType
print callable(getattr(object, method))

