# Selection Sort Program

arr = [64, 25, 12, 22, 11]

n = len(arr)

# Selection Sort
for i in range(n):

    # Assume current index is minimum
    min_index = i

    # Find the minimum element
    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the elements
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Display sorted array
print("Sorted Array:")
print(arr)