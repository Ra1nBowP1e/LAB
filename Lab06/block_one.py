import math

def cos_min(nums):
  if not isinstance(nums, list) or len(nums) != 4:
    print("Error: Input must be a list of 4 numbers.")
    return None
  try:
    min_num = min(nums)
    cos_min_num = math.cos(min_num)
    return cos_min_num
  except TypeError:
    print("Error: Input list must contain only numbers.")
    return None
  except ValueError:  
    print("Error: Invalid input for cosine calculation.")
    return None

numbers = [3.14, 1.57, 0.785, 2.0]
result = cos_min(numbers)
if result is not None:
  print(f"Косинус минимального числа: {result}")
