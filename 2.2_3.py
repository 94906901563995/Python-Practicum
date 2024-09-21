petya = int(input())
vasya = int(input())
tolya = int(input())
race = {petya: 'Петя', vasya: 'Вася', tolya: "Толя"}
print(race[max(vasya, petya, tolya)])
