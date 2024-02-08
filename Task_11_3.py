# Третья задача к одиннадцатому занятию


def decimal_to_roman(number):

    if number > 0:

        res = []
    
        dig_1 = number % 10
        if dig_1 < 4:
            res.insert(0, "I" * dig_1)
        if dig_1 == 4:
            res.insert(0, "IV")
        if 5 <= dig_1 < 9:
            res.insert(0, "V" + "I" * (dig_1 - 5))
        if dig_1 == 9:
            res.insert(0, "IX")
        number //= 10
        dig_2 = number % 10
        if dig_2 < 4:
            res.insert(0, "X" * dig_2)
        if dig_2 == 4:
            res.insert(0, "XL")
        if 5 <= dig_2 < 9:
            res.insert(0, "L" + "X" * (dig_2 - 5))
        if dig_2 == 9:
            res.insert(0, "XC")
        number //= 10
        dig_3 = number % 10
        if dig_3 < 4:
            res.insert(0, "C" * dig_3)
        if dig_3 == 4:
            res.insert(0, "CD")
        if 5 <= dig_3 < 9:
            res.insert(0, "D" + "C" * (dig_3 - 5))
        if dig_3 == 9:
            res.insert(0, "CM")
        number //= 10
        dig_4 = number % 10
        res.insert(0, "M" * dig_4)

    return "".join(res)


print(decimal_to_roman(int(input())))

# num = input()
# for i in range(1, len(num) + 1):
#     print((int(num) // 10 ** (len(num) - i)) % 10)  # нахождение каждой цифры числа
