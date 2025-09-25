def solve(arr, target):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l+r)//2
        mid = arr[m]
        if mid == target:
            return m
        if mid < target:
            l = m
        else:
            r = m
    return -1

test_array = [1,2,3,4,5,6,7,8,9]
print("Массив: ", test_array)

for target in [7, 1, 5, 10]:
    result = solve(test_array, target)
    if result > -1:
        print(f"Элемент {target} найден по индексу: {result}")
    else:
        print(f"Элемент {target} не найден")