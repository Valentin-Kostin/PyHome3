# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

count_arr = int(input('введите длину массива--> '))

arr_A = []

for i in range(count_arr):
    arr_A.append(int(input(f'запишите {i} число в массив--> ')))
num_X = int(input('введите число X--> '))
count_x = 0

arr_B = []
for i in range(count_arr):
    arr_B.append(arr_A[i] - num_X)
    if arr_B[i] < 0:
        arr_B[i] = arr_B[i] * -1
print(count_arr)
print(*arr_A,)       
for i in range(count_arr):
    if arr_B[i] == min (arr_B):
        print(f'{num_X} -> {arr_A[i]} ({i+1} число в массиве)')



