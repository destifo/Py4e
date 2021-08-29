# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
kwlcount = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    pos1 = line.find(':')
    newstr = line[pos1 + 1:]
    total = total + float(newstr.strip())
    kwlcount = kwlcount + 1


print("Average spam confidence:", total/kwlcount)
