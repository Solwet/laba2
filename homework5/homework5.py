def get_number():
    for number in range(30):
        if number % 2 != 0:
            yield number

odd_numbers = get_number()

values = []

for index, value in enumerate(odd_numbers):
    values.append(value)
    if len(values) == 5: 
        break

for value in odd_numbers:
    values.append(value)

first_value = values[0] if len(values) > 0 else None  
fifth_value = values[4] if len(values) > 4 else None 
last_value = values[-1] if len(values) > 0 else None

print(f"Первое нечетное число: {first_value}")
print(f"Пятое нечетное число: {fifth_value}")
print(f"Последнее нечетное число: {last_value}")