#REGEX PRACTICE
#greedy vs non-greedy
#unexpected results and stuff


import re #to import regular expressions library
x = "From stefen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("\S+@\S+",x) #greedy , re.findall returns a list of strings
print(y)
z = re.findall("\S+?@\S+",x) 
print(z)
w = re.findall("\S+?@\S+?",x)  #the pattern finds the smallest possible matches that fit the non-greedy requirement
print(w)

#\S+? first matches up to stefen.marquard, then stops when it encounters @. 
# \S+? after the @ matches as few characters as possible, stopping at u.
#I think it's because it goes from left to right 
#so yeah, quite odd, even I expected d@uct.ac.za at first for z but it takes values until the @ is encountered