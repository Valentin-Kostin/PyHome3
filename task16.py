# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5  1 2 3 4 5
# 3 -> 1

count_arr = int(input('введите длину массива--> '))

arr_A = []

for i in range(count_arr):
    arr_A.append(int(input(f'запишите {i} число в массив--> ')))
num_X = int(input('введите число X--> '))
count_x = 0
for i in range(count_arr):
    if arr_A[i] == num_X:
        count_x += 1
        

print(count_arr)
print(*arr_A,)
print(f'{num_X} -> {count_x}')
