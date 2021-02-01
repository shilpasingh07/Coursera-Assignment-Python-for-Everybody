#Program to print email address in a file

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line.rstrip()
    wd=line.split()
    if len(wd)<1:
        continue
    if wd[0]=='From':
        count=count+1
        print(wd[1])

print("There were", count, "lines in the file with From as the first word")