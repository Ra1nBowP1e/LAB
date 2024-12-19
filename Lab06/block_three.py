def replace_a_with_o(input_string):
    modified_string = input_string.replace('a', 'o')
    num_characters = len(input_string)
    num_replacements = input_string.count('a') 
    return modified_string, num_replacements, num_characters


input_string = "abracadabra"
modified_string, replacements, characters = replace_a_with_o(input_string)

print(f"Исходная строка: {input_string}")
print(f"Измененная строка: {modified_string}")
print(f"Количество замен: {replacements}")
print(f"Количество символов: {characters}")


input_string = "banana"
modified_string, replacements, characters = replace_a_with_o(input_string)

print(f"\nИсходная строка: {input_string}")
print(f"Измененная строка: {modified_string}")
print(f"Количество замен: {replacements}")
print(f"Количество символов: {characters}")

input_string = "oooaooo"
modified_string, replacements, characters = replace_a_with_o(input_string)

print(f"\nИсходная строка: {input_string}")
print(f"Измененная строка: {modified_string}")
print(f"Количество замен: {replacements}")
print(f"Количество символов: {characters}")
