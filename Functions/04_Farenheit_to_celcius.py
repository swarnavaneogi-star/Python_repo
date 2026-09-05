def temperature(f):
    c= (f-32)*5/9
    return c

f=float(input("enter the temperature :"))
c=temperature(f)
print("The temperature in Celsius is: ", round(c,2))