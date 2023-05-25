import re
f = open("/Users/robertponikiewski/PycharmProjects/pythonProject6/pesel.txt")
count = 0
for line in f:
    words = re.split("..12.......", line.strip())
    if len(words) > 1:
        count+=1
print(count)
f.seek(0)
count = 0
for line in f:
    words = re.split(".........[02468].", line.strip())
    if len(words) > 1:
        count += 1
print(count)
people = {}
f.seek(0)
for line in f:
    year = line[0]+line[1]
    try:
        people[year]+=1
    except:
        people[year]=1
max = 0
year = 0
for key in people:
    if max < people[key]:
        max = people[key]
        year = key
print(year)
f.seek(0)
model = [1,3,7,9,1,3,7,9,1,3]
peseles = []
for line in f:
    digits = re.split("", line.strip())
    digits.pop()
    digits.pop(0)
    sum = 0
    for i in range(0, len(digits)-1):
        sum+=model[i]*int(digits[i])
    if sum % 10 == 0:
        if digits[-1] != "0":
            peseles.append(int(line.strip()))
    else:
        r = sum % 10
        if str(10-r) != digits[-1]:
            peseles.append(int(line.strip()))
peseles.sort()
for pesel in peseles:
    print(pesel)

