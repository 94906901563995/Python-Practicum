line1 = input()
line2 = input()
line3 = input()
lines = [line1, line2, line3]
lines.sort()
for i in range(len(lines)):
    if "зайка" in lines[i]:
        print(lines[i], len(lines[i]))
        break