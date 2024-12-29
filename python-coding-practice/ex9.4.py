#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


#fname = input('Enter the file name: ')
#if not fname = "mbox-short.txt":
 #   quit()
fh = open('mbox-short.txt')
names = dict()
for line in fh:
    if 'From ' in line:
        pos = line.find(' ')
        spos = line.find(' ', pos + 1)
        username = line[pos : spos - 1]
        print(username)
        
print(names)
        
