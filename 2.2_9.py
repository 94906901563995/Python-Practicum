name1 = input()
name2 = input()
name3 = input()
names = {ord(name1[0]): name1, ord(name2[0]): name2, ord(name3[0]): name3}
print(names[min(ord(name2[0]), ord(name1[0]), ord(name3[0]))])