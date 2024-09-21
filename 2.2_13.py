a = input()
b = input()
c = input()
digits = [a[0], a[1], b[0], b[1], c[0], c[1]]
for i in range(len(digits)):
    if digits.count(digits[i]) >= 3:
        print(digits[i])
        break