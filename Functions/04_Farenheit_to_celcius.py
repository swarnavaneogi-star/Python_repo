def temperature(f):
    c= (f-32)*5/9
    return c

f=float(input("enter the temperature :"))
print("The temperature in Celsius is: ", temperature(f))
