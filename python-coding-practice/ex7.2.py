fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    pos = line.find(':')
    reqline = line[pos+1:]
    stripline = reqline.lstrip()
    fline = float(stripline)
    total = total + fline
avg = total/count
print("Average spam confidence:",avg)