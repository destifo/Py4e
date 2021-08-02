hrs = input("Enter Hours:\n")
rate = input("Enter the rate:\n")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Invalid input, Please try again")
    quit()

if h > 40:
    pay = (r * h) + (0.5 * r) * (h-40)
else:
    pay = r * h

print(pay)
