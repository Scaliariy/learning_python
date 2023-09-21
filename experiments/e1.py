import glob

myfiles = glob.glob("../files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(filepath, ':')
        print(file.read())
