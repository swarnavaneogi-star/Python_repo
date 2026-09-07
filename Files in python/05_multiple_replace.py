words = ["idiot", "stupid", "dumbass", "fuck", "bullshit", "asshole", "fucking", "bastard"]

with open("paragraph.txt", "r") as f:
    content = f.read()

newContent = content

for word in words:
    newContent = newContent.replace(word, "#" * len(word))

print(newContent)

with open("replace.txt", "w") as f:
    f.write(newContent)