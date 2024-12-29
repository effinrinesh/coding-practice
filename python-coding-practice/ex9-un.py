#Write a Python program to read through the mbox-short.txt file,
#  find the lines starting with "From", extract the email addresses,
#  and count how many times each email address appears. Finally, 
# print out the counts sorted by email address.


filename = input("Please enter the file name: ")
try:
    fh = open(filename)
except:
    print("Enter a valid file name")
mailid = dict()
for line in fh:
    if line.startswith("From:"):
        pos = line.find(" ")
        atpos = line.find(" ", pos+1)
        mailid = line[pos+1:atpos]
        #quickly refresh histogram creation & .get method and come back
    

