#Program to display largest and smallest number entered in loop

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        n=int(num)
    except:
        print("Invalid input")
        continue
        
    if largest is None:
        largest=n
        smallest=n
    elif n<smallest:
        smallest=n
    elif n>largest:
        largest=n

print("Maximum is", largest)
print("Minimum is", smallest)