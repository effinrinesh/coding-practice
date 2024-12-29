text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":") #search for a pattern in the requirement
val = text[pos+1:]
strpval = val.lstrip()
num = float(strpval)
print(num)