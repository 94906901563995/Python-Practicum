a = input()
b = input()
digits = [a[0], a[1], b[0], b[1]]
for i in range(4):
    digits[i] = int(digits[i])
digits.sort()
print(digits[3] * 100 + int(str(digits[2] + digits[1])[-1]) * 10 + digits[0])