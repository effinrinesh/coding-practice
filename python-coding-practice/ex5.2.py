largest = None
smallest = None
num = 0
while True:
    num = input()
    if num == "done":
        break
    #error checking
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
        
    #checking for none
    if largest == None:
        largest = fnum
        l=num

    if fnum > largest:
        largest = fnum
        l=num

    if smallest == None:
        smallest = fnum
        s=num

    if fnum < smallest:
        smallest = fnum
        s=num


print("Maximum is", l)
print('Minimum is', s) 