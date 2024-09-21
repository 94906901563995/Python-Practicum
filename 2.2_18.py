a = int(input())
b = int(input())
c = int(input())
sides = [a, b, c]
sides.sort()
if sides[2] ** 2 == (sides[1] ** 2 + sides[0] ** 2):
    print("100%")
elif sides[2] ** 2 >= (sides[1] ** 2 + sides[0] ** 2):
    print("велика")
else:
    print("крайне мала")