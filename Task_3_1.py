# Первая задача к третьему занятию

total, counter = 0, 0
while True:
    salary = float(input())
    if salary == 0:
        break
    total += salary
    counter += 1
if counter == 0:
    print("Error")
else:
    print(total / counter)
