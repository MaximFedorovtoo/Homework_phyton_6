# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# pytest -v tests\test_30.py

def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    """Возвращает список арифметической прогрессии по заданным:
    1) первый элемент
    2) разность
    3) количество элементов"""

    progresion = [first]
    if quantity == 0:
        progresion = []
        return progresion
    else:
        for i in range(quantity-1):
            progresion.append(progresion[i] + diff)
        return progresion

first = int(input("ВВедите первый элемент "))
diff = int(input("Введите разность "))
quantity =  int(input("Введите количество элементов "))
print(arithmetic_progression(first, diff, quantity))