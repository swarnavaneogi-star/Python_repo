with open ("this.txt","r") as f :
    content = f.readlines()

with open ("this_copy.txt","w") as f:
    for line in content:
        f.write(line)