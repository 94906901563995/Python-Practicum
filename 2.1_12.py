a = input()
b = input()
maxnumber = str(max(int(a), int(b)))
numbers = []
for i in range(len(maxnumber)):
    numbers.append(maxnumber[i])
result = ''
for i in range(1, min(len(a), len(b)) + 1):
    numbers[-i] = str(int(a[-i]) + int(b[-i]))[-1]
for i in range(len(numbers)):
    result = result + numbers[i]
print(result)