import * from urllib

fh = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fh:
    print(line.decode().strip())

#like a file
count = dict()
for line in fh:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
