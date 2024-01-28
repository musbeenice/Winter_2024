# Первая задача к шестому занятию

rome = input()

roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
roman_spec = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

total = 0
i = 0

while i < len(rome):
    if rome.startswith(tuple(roman_dict), i):  # == True
        total += roman_dict[rome[i : i + 1]]
        i += 1
    if rome.startswith(tuple(roman_spec), i):
        total += roman_spec[rome[i : i + 2]]
        i += 2

print(total)
