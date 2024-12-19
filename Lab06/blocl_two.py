
def average_grade():
    grades = []
    for i in range(20):
        while True:
            try:
                grade = float(input(f"Введите оценку {i+1}-го ученика: "))
                if 0 <= grade <= 10: 
                    grades.append(grade)
                    break
                else:
                    print("Оценка должна быть в диапазоне от 0 до 10.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")

    average = sum(grades) / len(grades)
    print(f"Средняя оценка по физике: {average:.2f}")

average_grade()


