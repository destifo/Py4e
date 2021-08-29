fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    wordlst = line.split()
    #if len(wordlst) < 2 is checked first incase there is an lsi with smaller index
    #to avoid the 2nd test in the if statement
    if len(wordlst) < 2 or wordlst[0] != 'From':
        continue
    else:
        print(wordlst[1])
        count = count +1


print("There were", count, "lines in the file with From as the first word")
