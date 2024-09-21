petya = int(input())
vasya = int(input())
tolya = int(input())
race = {petya: 'Петя', vasya: 'Вася', tolya: "Толя"}
d = [petya, vasya, tolya]
d.sort()
print(f"1. {race[d[2]]}")
print(f"2. {race[d[1]]}")
print(f"3. {race[d[0]]}")