numbers = input("Введите последовательность чисел через пробел: ").split()
s = set()

for number in numbers:
    if number in s:
        print("YES")
    else:
        print("NO")
        s.add(number)