count = 0
total = 0
print('Before  ', count ,'   ' , total)
for num in [9,41,12,3,74,15]:
    count = count+1
    total = total+num
    print(count,'  ',total,'  ',num)
print('After   ', count ,'   ', total, '  ',total/count)