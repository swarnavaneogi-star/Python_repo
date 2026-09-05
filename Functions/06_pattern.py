def pat(n):
    if (n==0):
        return
    print("*" * n)
    pat(n-1)

n=int(input("Enter the number of rows: "))
result = pat(n)