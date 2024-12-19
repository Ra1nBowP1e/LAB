a = float(input("Введите число A (A > 1): "))

if a <= 1:
  print("Число A должно быть больше 1.")
else:
  k = 0
  sum_harmonic = 0
  while sum_harmonic < a:
    k += 1
    sum_harmonic += 1 / k

  print(f"Наибольшее целое число K: {k -1}")
  print(f"Сумма 1 + 1/2 + ... + 1/(K-1): {sum_harmonic - 1/k}")




