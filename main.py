import sys

size = int(input('Введите размер массива: '))

if size < 2:
    print("сории, ничего не получится, введите другой размер массива1")
    sys.exit()

arr = []

for i in range(size):
    el = int(input(f'Введите элемент {i + 1}: '))
    arr.append(el)

print(arr)

for i in range(size-1):
    for j in range(size-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]



print(arr)