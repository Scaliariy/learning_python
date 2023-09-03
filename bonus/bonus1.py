contents = ["ADxxcxcx xcxhgg adads", "BVVCS adasda ;l;lfg sd", "FDGDFLGLDFLK fgdd;dsf"]

filenames = ["Nicol.txt", "Andrew.txt", "Ann.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
    file.close()

