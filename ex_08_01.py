#the program reads through a file and splits the lines into words
#and then sort the words alpabetically before checking for word repitition
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    temp = line.split()
    #print(temp)
    for words in temp:
        if not words in lst:
            lst.append(words)
        else:
            continue

lst.sort()
print(lst)
