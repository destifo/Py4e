import re

fh = open("regex_sum_1323255.txt")
numlist = list()

for line in fh:
    line = line.rstrip()
    returnval = re.findall('[0-9]+', line)
    for i in range(len(returnval)):
        if len(returnval) != 0:
            numlist.append(int(returnval[i]))


print(sum(numlist))
