#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour
#  of the day for each of the messages. You can pull the hour out from 
# the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

fname = input("Enter file name: ")
if len(fname)<1: fname = "mbox-short.txt"
hourcount = dict()
fhandle = open(fname)
for lines in fhandle:
    if lines.startswith("From "):
        pos = lines.find(":")
        key = lines[pos-2 : pos]   #remember parsing & extraction
        hourcount[key] = hourcount.get(key,0) + 1

hourlist = sorted(hourcount.items())
for hour,count in hourlist:
    print(hour,count)