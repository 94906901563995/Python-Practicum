n = int(input())
m = int(input())
t = int(input())
t = (t + n * 60 + m) % 1440
minutes = str(t % 60)
if len(minutes) == 1:
    minutes = '0' + minutes
hours = str(t // 60)
if len(hours) == 1:
    hours = '0' + hours
print(f"{hours}:{minutes}")