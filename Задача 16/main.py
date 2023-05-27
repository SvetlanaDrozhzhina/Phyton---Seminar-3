N = abs(int(input("Введите количество элементов в массиве: ")))
A_entered = input("Введите элементы массива через пробел: ").split()
A_num = list(map(int, A_entered))
X = int(input("Введите число, которое необходимо найти: "))
count = 0
for i in range(N):
    if A_num[i] == X:
        count += 1
print("Число встречается: ", count)