def selection_sort(data):
    for i in range(len(data)):

        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        
        data[i], data[min_index] = data[min_index], data[i]

data = [64, 25, 12, 22, 11]
selection_sort(data)

print("Sorted Data:")
print(data)