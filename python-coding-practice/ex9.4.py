#9.4 Write a program to read through the mbox-short.txt and figure 
# out who has sent the greatest number of mail messages. The program
#  looks for 'From ' lines and takes the second word of those lines as 
# the person who sent the mail. The program creates a Python dictionary
#  that maps the sender's mail address to a count of the number of times they
#  appear in the file. After the dictionary is produced, the program reads
#  through the dictionary using a maximum loop to find the most prolific committer.
'''
fh = open("mbox-short.txt")
mailid = dict()
for line in fh:
    if line.startswith("From "):
        pos = line.find(' ')
        endpos = line.find(' ', pos + 1)
        key = line[pos+1:endpos]
        mailid[key] = mailid.get(key,0) + 1
#max looping through the dictionary
bigname = None
bigval = None
for mailname,mailcount in mailid.items():
    if bigval is None or mailcount > bigval:
        bigval = mailcount
        bigname = mailname

print(bigname,bigval)

'''
#another cleaner way using .split() method

fh = open("mbox-short.txt")
mailid = dict()
words = list()
for line in fh:
    words = line.split() #default delimiter is a space and treats many spaces consecutively as single space
    if not "From" in words: continue #skip code
    for i in range(len(words)): #range gives a list of indices while the len just gives a fixed value
        if words[i] == "From":
            key = words[i+1]
            mailid[key] = mailid.get(key,0) + 1  #histogram idiom
#max looping through the dictionary
bigname = None
bigval = None
for mailname,mailcount in mailid.items():
    if bigval is None or mailcount > bigval:
        bigval = mailcount
        bigname = mailname

print(bigname,bigval)       
