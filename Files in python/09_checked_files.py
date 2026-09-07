with open ("file_1.txt","r") as f:
    content_1=f.read()

with open ("file_2.txt","r") as f:
    content_2=f.read()

if (content_1==content_2):
    print("Yes, The files are identical.")
else :
    print("No , the files are not identical")   