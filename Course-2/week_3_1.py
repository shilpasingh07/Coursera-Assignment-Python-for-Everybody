#Program to open and handle file

#Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lx=fh.read()
nl=lx.strip()
print(nl.upper())