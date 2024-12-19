def find_max_and_index(arr):
    if not arr:
        return None, None

    max_element = arr[0]
    max_index = 0
    for i, num in enumerate(arr):
        if num > max_element:
            max_element = num
            max_index = i
    return max_element, max_index



my_array = [1, 5, 2, 8, 3, 9, 4, 7, 6]
max_val, max_idx = find_max_and_index(my_array)
print(f"Максимальный элемент: {max_val}, Индекс: {max_idx}") 



