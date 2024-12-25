def counting_sort(arr):
    min_value = min(arr)
    max_value = max(arr)

    count = [0] * (max_value - min_value + 1)
    for num in arr:
        count[num - min_value] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num - min_value] -= 1
        output[count[num - min_value]] = num
    for i in range(len(arr)):
        arr[i] = output[i]

arr = [1, 3, 7, 8, 6, 1, 9, 5]
print("original Array ", arr)
counting_sort(arr)
print("Sorted Array ", arr)