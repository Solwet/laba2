import random

def find_multiples():
    numbers = [random.randint(0, 200) for _ in range(10)]
    print("Сгенерированные числа:", numbers)

    while True:
        x = input("Введите цифру X для поиска кратных: ")
        
        if x.isdigit() and 0 <= int(x) <= 9:
            x = int(x)
            break
        else:
            print("Пожалуйста, введите цифру от 0 до 9.")

    if x == 0:
        print("Для 0 все числа кратные.")
        multiples = list(numbers)
    else:
        multiples = list(filter(lambda num: num % x == 0, numbers))
    
    if multiples:
        print(f"Числа, кратные {x}: {multiples}")
    else:
        print(f"Нет чисел, кратных {x}.")

find_multiples()