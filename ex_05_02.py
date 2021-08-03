smallest_so_far = None
largest_so_far = None

#This block of code accepts list of numbers from the user and finds the max and min no from the given inputs
#It returns an error upon a non numeric value is given as an input and asks for an input again
#The program terminates and displays the results when "done" is given as an input.
while True:
    num = input("Enter a no:\n")

    if num == "done":
        break

    try:
        fval = float(num)
    except:
        print("Invalid input")
        continue

    if smallest_so_far is None:
        smallest_so_far = fval
    elif smallest_so_far > fval:
        smallest_so_far = fval

    if largest_so_far is None:
        largest_so_far = fval
    elif largest_so_far < fval:
        largest_so_far = fval

print("Maximum is ", largest_so_far)
print("Minimum is ", smallest_so_far)
