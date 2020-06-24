handle = open('mbox-short.txt')
hours = [line.rstrip().split()[5].split(':')[0] for line in handle if line.startswith('From ')]
print(hours)
count = {}
for hour in hours:
	count[hour] = count.get(hour,0) + 1
hours = sorted([(k,v) for k,v in count.items()])
for hour in hours:
	print(hour[0],hour[1])

# c = {'a':10,'b':1,'c':22}
# # [exepression for variables in data_structure if expression] --> list comprehension
# tmp = [(v,k) for k,v in c.items()]
# print(tmp[0][1])
# tmp = sorted(tmp,reverse=True)
# print(tmp)


# c = {'a':10,'b':1,'c':22}
# tmp = []
# for k,v in c.items():
# 	tmp.append((v,k))
# print(tmp)
# tmp = sorted(tmp,reverse=True)
# print(tmp)