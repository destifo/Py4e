import re

fh = open("regex_sum_42.txt")
numlist = list()
total = 0


for line in fh:
    line = line.rstrip()
    returnval = re.findall('[0-9]+', line)
    for i in range(len(returnval)):
        total += int(returnval[i])

print(total)
