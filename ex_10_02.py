fname = input("Enter the file name:")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
words = list()
calendar = list()
daylist = dict()

for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != "From":
        continue

    calendar = words[5].split(":")
    if calendar[0] in daylist:
        daylist[calendar[0]] = daylist[calendar[0]] + 1
    else:
        daylist[calendar[0]] = 1

hrorder = sorted([ (k, v) for k,v in daylist.items() ])

for k,v in hrorder:
    print(k, v)
