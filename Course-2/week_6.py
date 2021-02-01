#Program to print hour distribution of message in a file

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic=dict()

for line in handle:
    line.rstrip()
    wd=line.split()
    if len(wd)>1 and wd[0]=='From':
        wwd=wd[5].split(":")
        dic[wwd[0]]=dic.get(wwd[0],0)+1
            
big=0
li=list()
for k,v in dic.items():
    li.append((k,v))
li.sort()
for l1 in li:
    print(l1[0],l1[1])