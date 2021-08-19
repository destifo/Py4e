fname = input("Enter the file name:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
userCount = dict()

for line in fh:
    line = line.rstrip()
    words = line.split()
    print(words)
    if len(words) < 1 or words[0] != "From":
        continue
    else:
        userCount[words[1]] = userCount.get(words[1], 0) + 1

bigWord = None
bigCount = None
for k in userCount:
    if bigCount is None or userCount[k] > bigCount:
        bigWord = k

bigCount = userCount[k]

print("The user", bigWord, "sent the most messages", bigCount, "times")
