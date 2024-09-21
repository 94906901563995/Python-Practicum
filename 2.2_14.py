a = input()
anydigits = []
digits = []
for i in range(len(a)):
    anydigits.append(int(a[i]))
    if a[i] != '0':
        digits.append(int(a[i]))
anydigitsclone = list(anydigits)
clonedigits = list(digits)
minimum = min(clonedigits) * 10
anydigitsclone.remove(min(clonedigits))
minimum = minimum + min(anydigitsclone)
anydigitsclone = list(anydigits)
clonedigits = list(digits)
maximum = max(clonedigits) * 10
anydigitsclone.remove(max(clonedigits))
maximum = maximum + max(anydigitsclone)
print(f"{minimum} {maximum}")