fileName = input('Enter file:')
if len(name) < 1 : name = "mbox-short.txt"
fh = open(fileName)
count = {}

for line in fh:
    if line.startswith('From '):
        words = line.split()
        count[words[1]] = count.get(words[1],0) + 1

words = list(count.keys())
values = list(count.values())
print(type(words))
print(type(values))

bigcount = max(values)
bigword_index = values.index(bigcount)

bigword = words[bigword_index]

print(bigword,bigcount)