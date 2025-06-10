# f = open("sample.txt") #for only reading the file
# print(f.read())

with open("sample.txt", 'a') as f:
    f.write("this is new line in file")

with open("sample.txt", 'r')as f:
    print(f.read())