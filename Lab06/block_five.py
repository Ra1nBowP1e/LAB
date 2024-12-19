def find_divisible_by_digits(n):
    result = []
    for i in range(1, n + 1):
        if is_divisible_by_digits(i):
            result.append(i)
    return result


def is_divisible_by_digits(num):
    s_num = str(num)
    for digit in s_num:
        digit = int(digit)
        if digit == 0 or num % digit != 0:
            return False
    return True

n = 20
numbers = find_divisible_by_digits(n)
print(f"Числа, не превосходящие {n}, которые делятся на каждую из своих цифр: {numbers}")





def print_digits_reversed(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)  
        print_digits_reversed(n // 10) 


print_digits_reversed(12345) 
print("\n")
print_digits_reversed(987)  
print("\n")
print_digits_reversed(1)    


