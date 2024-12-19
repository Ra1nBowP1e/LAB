def get_odd_numbers_descending(arr):
    odd_numbers = [num for num in arr if num % 2 != 0]
    if not odd_numbers:
        return None 
    odd_numbers.sort(reverse=True)
    return odd_numbers


my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = get_odd_numbers_descending(my_array)
if result:
    print(f"Нечетные числа в порядке убывания: {result}")
else:
    print("Нет нечетных чисел в массиве.")


my_array2 = [2, 4, 6, 8]
result2 = get_odd_numbers_descending(my_array2)
if result2:
    print(f"\nНечетные числа в порядке убывания: {result2}")
else:
    print("Нет нечетных чисел в массиве.")

