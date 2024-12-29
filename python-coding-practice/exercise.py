hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
extra = 0
if h<=40:
    pay = h*r
else:
    extra = (h-40)*1.5*r
    pay = (40*r) + extra
print('Gross pay:',pay)