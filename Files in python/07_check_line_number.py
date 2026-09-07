with open ("log.txt","r") as f:
    lines = f.readlines()

line_number = 1
for line in lines:
    if "python" in line:
        print(f"Python found in line {line_number}")
        break
    line_number += 1

else:
    print("Python not found in any line.")