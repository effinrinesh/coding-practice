def computepay(h, r):
    if(h<=40):
        pay = h*r
        return pay
    else:
        pay = (40*r)+(h-40)*r*1.5
        return pay
    
hrs = input("Enter Hours:")
rt = input("Enter Rate:")
hours = float(hrs)
rate = float(rt)
p = computepay(hours,rate)
print("Pay", p)