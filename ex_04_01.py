def computepay(a, b):
    if h > 40:
        pay = (b * a) + (0.5 * b) * (a - 40)
    else:
        pay = (b * a)
    return pay

hrs = input('Enter the number of hours:\n')
rate = input('Enter your hourly rate:\n')

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, Enter a numerical value")

pay = computepay(h, r)
print("Pay", pay)
