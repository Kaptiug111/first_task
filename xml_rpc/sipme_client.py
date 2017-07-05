import xmlrpclib

s = xmlrpclib.ServerProxy('http://127.0.0.1:8000')
print s.selectAll()
print s.selectByID()
print s.insert()
print s.delete()
print s.selectAll()