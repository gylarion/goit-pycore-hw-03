import random

def get_numbers_ticket(min, max, quantity):
    """ 1) Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
        2) Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися.
        Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список."""
    if not (1 <= min < max <= 1000):
        return []
    if not (0 < quantity <= (max - min + 1)):
        return []
    return sorted(random.sample(range(min, max + 1), quantity))


lottery_numbers = get_numbers_ticket(1, 500, 6)
print("Лотерейні номери із вашого квитка:", lottery_numbers)
