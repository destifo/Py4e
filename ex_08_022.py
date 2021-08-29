fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
wordlst = []
for lines in fh:
    if not lines.startswith('From'):
        continue
    else:
        wordlst = lines.split()
        print(wordlst[1])
        count = count + 1


print("There were", count, "lines in the file with From as the first word")
