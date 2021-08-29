'''# opens a file after recieving from a user and reads through that file by displaying
on the console
'''
fname = input("Enter file name: ")
fh = open(fname)
for lines in fh:
    lines = lines.rstrip()
    print(lines)
