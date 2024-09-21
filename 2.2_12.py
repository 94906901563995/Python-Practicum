a = int(input())
b = int(input())
c = int(input())
if (a + b > c) and (a + c > b) and (b + c > a) and (0 not in (a, b, c)):
    print("YES")
else:
    print("NO")