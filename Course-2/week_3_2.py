#Program to handle file

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        lx=line.find(":")
        nl=float(line[lx+1:])
        total=total+nl
        count=count+1
print("Average spam confidence:",total/count)