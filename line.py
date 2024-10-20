file = open('file.txt','r')
c = 0
content = file.read()
list = content.split("\n")
for i in list:
    if i:
        c = c+1
print(c)
file.close()