#Program to print email with highest freguency in a file

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic=dict()

for line in handle:
    line.rstrip()
    wd=line.split()
    if len(wd)>1 and wd[0]=='From':
        for word in wd[1:2]:
            dic[word]=dic.get(word,0)+1
            
big=0
for k,v in dic.items():
    if v>big:
        big=v
        bigkey=k

print(bigkey,dic[bigkey])