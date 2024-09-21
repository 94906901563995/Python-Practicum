a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
else:
    if (b ** 2 < 4 * a * c) or (a == 0 and b == 0):
        print("No solution")
    else:
        if a != 0:
            discriminant = b ** 2 - 4 * a * c
            root1 = (discriminant ** 0.5 - b) / (2 * a)
            root2 = (0 - discriminant ** 0.5 - b) / (2 * a)
            roots = [root1, root2]
            roots.sort()
            if root1 != root2:
                print(f"{roots[0]:.2f} {roots[1]:.2f}")
            else:
                root = (0 - b) / (2 * a)
                print(f"{root:.2f}")
        else:
            root = (0 - c) / b
            print(f"{root:.2f}")