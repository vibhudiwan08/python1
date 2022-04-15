wordCount=1
characterCount=0
sent=input("Enter your introduction")
print(sent)

for i in sent :
    characterCount=characterCount+1
    if (i == ' ') :
        wordCount=wordCount+1

print("Number of words in the line are :", wordCount)
print("Number of characters in the line are :", characterCount)