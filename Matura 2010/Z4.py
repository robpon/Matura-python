import re
f = open("anagram.txt")
index = 1
for line in f:
    words = line.strip().split(" ")
    fWL = len(words[0])
    fA = re.split("", words[0])
    fA.sort()
    sameL = True
    sameA = True
    for word in words:
        nA = re.split("", word);
        nA.sort()
        if fA != nA:
            sameA = False

        if fWL != len(word):
            sameL = False

    if sameL == True:
        print("Same L", line)
    if sameA == True:
        print("Same A", line)

    index+=1
