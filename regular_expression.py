import re
print( sum( [ float(number) for number in re.findall('[0-9]+',open('regex_sum_604780.txt').read()) ] ) )

# import re

# file = open('regex_sum_604780.txt')
# sum = 0
# for line in file:
#     line = line.rstrip()
#     numbers = re.findall('[0-9]+',line)
#     for i in range(len(numbers)):
#         sum = sum + float(numbers[i])

# print(sum)
# extracting data with regular expression 
# if we need the real character as $ --> \$ , \ before the return

# hand = open('mbox-short.txt')
# for line in hand:
# 	line = line.rstrip()
# 	## get out email
# 	## parentheses determine the start and the end, not a part of the return
# 	if re.findall('\S+?@\S+',line):	
# 		print(re.findall('\S+?@\S+',line))

# hand = open('mbox-short.txt')
# for line in hand:
# 	line = line.rstrip()
# 	## findall working with greedy matching
# 	## if it ends with more than one : it will return the largest 
# 	## id we add ? it won't be greedy
# 	if re.findall('^F.+?:',line):	
# 		print(re.findall('^F.+?:',line))

# hand = open('mbox-short.txt')
# for line in hand:
# 	line = line.rstrip()
# # 	[0-9] fr0m 0 to 9 numbers as string and return a list of strings
# 	if re.findall('[0-9]+',line):			  
# 		print(re.findall('[0-9]+',line))

# searching for data with regular expression 

# hand = open('mbox-short.txt')
# for line in hand:
# 	line = line.rstrip()
## ^ start with 'From:', . character match any character 
## * zero or more , \S non whitespace charcter , + one or more
# 	if re.search('^X-\S+:',line):  
# 								   
# 		print(line)

# hand = open('mbox-short.txt')
# for line in hand:
# 	line = line.rstrip()
# 	if line.find('From:') >= 0:
# 		print(line)