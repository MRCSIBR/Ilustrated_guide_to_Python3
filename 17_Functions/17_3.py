#17.2 Busqueda Binaria

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

result = binary_search(array, target)
if result != -1:
    print("El objetivo se encuentra en el índice:", result)
else:
    print("El objetivo no se encontró en el array.")
