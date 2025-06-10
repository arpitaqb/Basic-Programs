def myfunc(n):
     
    return lambda a : a * n 

print(myfunc(12))
mydoubler = myfunc(2)

print(mydoubler([11, 12 ,17]))
print(mydoubler(10))