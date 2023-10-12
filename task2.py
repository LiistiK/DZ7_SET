n = int(input('Кол-во чисел в первом списке: '))
l1 = []
for i in range(n):
    l1.append(int(input('Введите число: ')))

n2 = int(input('Кол-во чисел во втором списке: '))
l2 = []
for i in range(n2):
    l2.append(int(input('Введите число: ')))

print(set(l1).intersection(set(l2)))