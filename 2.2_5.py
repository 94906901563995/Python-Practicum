n = int(input())
m = int(input())
petya = 6 + n
vasya = 9 + m
apples = {petya: 'Петя', vasya: 'Вася'}
print(apples[max(vasya, petya)])