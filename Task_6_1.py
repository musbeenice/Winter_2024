# Первая задача к шестому занятию


def roman_to_decimal(number):
    dct = {
        "CM": 900,
        "CD": 400,
        "XC": 90,
        "XL": 40,
        "IX": 9,
        "IV": 4,
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    res = 0
    while number != "":
        for i in dct:
            if number.startswith(i):
                res += dct[i]
                number = number[len(i):]  # срезаем пройденную(ые) букву(ы)!
                print(i, dct[i], res)
                break
    return res


print(roman_to_decimal(input()))
