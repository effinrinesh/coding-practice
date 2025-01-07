#Write a Python program to read through the mbox-short.txt file,
#  find the lines starting with "From", extract the email addresses,
#  and count how many times each email address appears. Finally, 
# print out the counts sorted by email address.


filename = input("Please enter the file name: ")

try:
    fh = open(filename)
except:
    print("Enter a valid file name")
    quit()
    
mailid = dict()

for line in fh:
    if line.startswith("From:"):
        pos = line.find(" ")
        atpos = line.find(" ", pos+1)
        key = line[pos+1:atpos]
        mailid[key] = mailid.get(key,0) + 1
        
print(mailid)
       # if key in mailid:
        #    mailid[key] = mailid[key] + 1
       # else:
        #    mailid[key] = 1
        #quickly refresh histogram creation concepts & .get method and come back
        # okay key value pairs are kinda clear now
        # learn histogram idioms
#practicing a bit for max looping
#print(mailid)
#bignum = None
#bigname = None
#for kk,vv in mailid.items():
#    if bignum is None or vv > bignum:
#        bignum = vv
#        bigname = kk
#print(bigname,bignum)