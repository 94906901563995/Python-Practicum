petya = int(input())
vasya = int(input())
tolya = int(input())
race = {petya: 'Петя', vasya: 'Вася', tolya: "Толя"}
d = [petya, vasya, tolya]
d.sort()
print(f"{race[d[2]]:^24}")
print(f"{race[d[1]]:^8}")
print(" " * 16 + f"{race[d[0]]:^8}")
print("{:^8}".format("II") + "{:^8}".format("I") + "{:^8}".format("III"))