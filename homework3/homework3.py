from datetime import datetime

def age():
    while True:
        birth_date = input("Введите дату рождения в формате день/месяц/год (например, 06/05/2004): ")
        
        try:
            birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
            
            today = datetime.today()

            if birth_date > today:
                print("Дата рождения не может быть в будущем. Попробуйте снова.")
                continue
            
            age = today.year - birth_date.year
            
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            
            print(f"Ваш возраст: {age} лет")
            break
        
        except ValueError:
            print("Неверный формат даты или несуществующая дата. Попробуйте снова.")

age()