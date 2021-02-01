#Program to make list of words in a file

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    wd=line.split()
    for word in wd:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)