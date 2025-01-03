#An problem from the course I've taken that I'm gonna try before
#I see the prof explainination (lel too many ins)
#Anyways, the problem is to find the top 10 occuring words in a text file

#read and break the file into mutable data structures of words
fname = input("Enter file name: ")
if len(fname)<1: fname = "romeo.txt"  #default val so yaknow we can just hit enter and keep checking if the code works
#sooo here's my thought process, take file, read through lines, split lines get words, 
# create a dictionary (histogram) and then .items() to get list of tuples of (Value,Key) pair (not key, value) 
# so it's a data structure that can be ordered (AHHHH DON'T STRIVE FOR PERFECTION REMEMBER CAPTAIN MAYURI'S MONOLOGUE)
# then arrange them in descending order then print the corresponding tuple until 10th value

#ok lets start (I'm journaliing while i type OK these are my practice files and yes I do know & follow the best practices)

fhandle = open(fname)
wdlist = list()
dictwd = dict()
itemlst = list()
for lines in fhandle:
    lines = lines.rstrip()
    wdlist = lines.split()
    #print(wdlist)
    for word in wdlist:
        dictwd[word] = dictwd.get(word,0) + 1
    
itemlst = dictwd.items()
#print(itemlst)
tmp = tuple()
newlst = list()
#NOW WE CREATE A LIST OF TUPLE AND SWAP THE KEY VALUE PAIRS
for key,value in itemlst: # or you can also put for (key,value) in itemlst:
    tmp = (value,key)
    newlst.append(tmp)
#now we sort the value,key tuple in the list
newlst = sorted(newlst, reverse=True) #sorted() returns a sorted list

print(newlst[0:10])