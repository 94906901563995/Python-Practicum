n = input()
digits = [int(n[0]), int(n[1]), int(n[2])]
digits.sort()
if (digits[0] + digits[2]) == digits[1] * 2:
    print("YES")
else:
    print("NO")