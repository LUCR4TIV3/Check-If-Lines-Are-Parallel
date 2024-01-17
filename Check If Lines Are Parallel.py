a = None
while not isinstance(a, int):
    try:
        a = int(input("What's your x coefficient, in the line, with the form ax+by=c."))
    except ValueError:
        print("Invalid inputW Please enter a valid value.")

b = None
while not isinstance(b, int):
    try:
        b = int(input("What's your y coefficient, in the line, with the form ax+by=c."))
    except ValueError:
        print("Invalid input! Please enter a valid value.")
sign = '+' if b >= 0 else ''
c = None
while not isinstance(c, int):
    try:
        c = int(input("What's your c value, in the line, with the form ax+by=c."))
    except ValueError:
        print("Invalid input! Please enter a valid value.")

print(f"{a}x{sign}{b}y={c}")
print("\n")


print("Now for your second line...\n")

a2 = None
while not isinstance(a2, int):
    try:
        a2 = int(input("What's your second x coefficient, in the line, with the form ax+by=c."))
    except ValueError:
        print("Invalid input! Please enter a valid value.")

b2 = None
while not isinstance(b2, int):
    try:
        b2 = int(input("What's your second y coefficient, in the line, with the form ax+by=c."))
    except ValueError:
        print("Invalid input! Please enter a valid value.")
sign2 = '+' if b2 >= 0 else ''

c2 = None
while not isinstance(c2, int):
    try:
        c2 = int(input("What's your second c value, in the line, with the form ax+by=c."))
    except ValueError:
        print("Invalid input! Please enter a valid value.")

print(f"{a2}x{sign2}{b2}y={c2}")
print("\n")


arr = [a, b, c]
arr2 = [a2, b2, c2]

if arr == arr2:
    print(f"The lines {a}x{sign}{b}y={c} and {a2}x{sign2}{b2}y={c2} are parallel to themselves.")

else:
    try:
        slope = -a / b
        slope2 = -a2 / b2
    except ZeroDivisionError:
        if b == 0:
            slope = "The line is vertical, and the slope is undefined."
        if b2 == 0:
            slope2 = "The line is vertical, and the slope is undefined."
    if slope == slope2:
        print(f"The lines {a}x{sign}{b}y={c} and {a2}x{sign2}{b2}y={c2} are parallel to each other.")
    else:
        print(f"The lines {a}x{sign}{b}y={c} and {a2}x{sign2}{b2}y={c2} are not parallel to each other.")
