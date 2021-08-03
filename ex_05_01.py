n = 0
total = 0

while True:
    inval = input("Enter the no:\n")
    if inval == "done":
         break
    try:
         ifval = float(inval)
    except:
        print("Invalid Input")
        continue

    n = n + 1
    total = total + ifval

print(total, n, total/n)
