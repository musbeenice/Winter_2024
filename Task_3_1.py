# Первая задача к третьему занятию

total = 0
counter = 0
while True:
    salary = float(input())
    total += salary
    counter += 1
    if salary == 0:
        counter -= 1
        break
average = total / counter
print(average)
