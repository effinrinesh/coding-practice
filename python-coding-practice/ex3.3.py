score = input("Enter Score: ")
try:
    s = float(score)
except:
    print('Enter valid score')
    quit()
if(s>1):
    print('Enter valid score')
elif(s<0):
    print('Enter valid score')
elif(s>=0.9):
    print('A')
elif(s>=0.8):
    print('B')
elif(s>=0.7):
    print('C')
elif(s>=0.6):
    print('D')
elif(s<0.6):
    print('F')

