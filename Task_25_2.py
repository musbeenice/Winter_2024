# Вторая задача к двадцать пятому занятию


def is_palindrome(s):
    if len(s) <= 1:  # нужна именно такая проверка, из-за чётности/нечётности элементов
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


print(is_palindrome(input()))
