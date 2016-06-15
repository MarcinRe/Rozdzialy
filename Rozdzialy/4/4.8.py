print"---------------3.30----------------"
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print ["%s=%s" % (k,v) for k,v in params.items()]
print (";".join(["%s=%s" %(k,v) for k,v in params.items()]))
print"---------------3.31----------------"
li = ['pwd=secret', 'database=master', 'uid=sa', 'server=mpilgrim']
s=";".join(li)
print s
print s.split(";")
print s.split(";",1)