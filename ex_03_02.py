score = input("Enter Score:\n")
try:
    fscore = float(score)
except:
    print("Error, Please enter a numeric value")
    quit()

if fscore > 1.0 or fscore < 0.0:
    print("Error, insert a number between 1 and 0")
    quit()
elif fscore >= 0.9:
    print('A')
elif fscore >= 0.8:
    print('B')
elif fscore >= 0.7:
    print('C')
elif fscore >= 0.6:
    Print ('D')
else:
    print('F')
