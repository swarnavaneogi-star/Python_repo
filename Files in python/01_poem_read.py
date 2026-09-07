word = input ("Enter a word you want to search in the poem: ")
with open("poem.txt", "r") as f:
    content = f.read()

if word in content:
    print(f"{word} is present in the poem")
else:
    print(f"{word} is not present in the poem")