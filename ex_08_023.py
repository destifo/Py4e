fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
wordlst = []
for lines in fh:
    wordlst = lines.split()
    #print(wordlst[1])
    if not 'From' in wordlst:
        continue
    else:
        print(wordlst[1])
        count = count +1


print("There were", count, "lines in the file with From as the first word")
