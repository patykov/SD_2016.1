import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:8000')
print(proxy.pow(2,3))  # Returns 2**3 = 8
print(proxy.add(2,3))  # Returns 5
print(proxy.mul(5,2))  # Returns 5*2 = 10