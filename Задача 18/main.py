N = abs(int(input("Введите количество элементов массива: ")))
A_entered = input("Введите элементы массива через пробел: ").split()
A_num = list(map(int, A_entered))
X = int(input("Введите число X: "))
min = abs(X - A_num[0])
index = 0
for i in range(1, N):
    count = abs(X - A_num[i])
    if count < min:
        min = count
        index = i
print("Самый близкий по величине элемент к заданному числу: ", A_num[index])