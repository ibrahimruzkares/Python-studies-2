folder = open("/Users/sample/OneDrive/Desktop/new/sample.txt","r")
content = folder.read()
print(content)
folder.close()


with open("/Users/sample/OneDrive/Desktop/new/sample.txt","r") as folder:
    content = folder.read()
    print(content)