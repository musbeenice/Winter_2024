# Вторая задача к двадцать пятому занятию


def is_palindrome(string):
    def result_str(s):
        return [x for x in s.lower() if x.isalnum()]

    def are_chars_equal(s):
        if len(s) <= 1:  # нужна именно такая проверка, из-за чётности/нечётности элементов
            return True
        if s[0] != s[-1]:
            return False
        return are_chars_equal(s[1:-1])

    res_str = result_str(string)
    return are_chars_equal(res_str)


msg = input()
print(is_palindrome(msg))
