# Третья задача к двадцать четвертому занятию

def is_correct_bracket(text):
    if "(" in text and ")" in text and not text.isalnum():
        open_or_cl = 0
        if not text.startswith(")") and not text.endswith("("):
            for char in text:
                if char == "(":
                    open_or_cl += 1
                elif char == ")":
                    open_or_cl -= 1
                    if open_or_cl < 0:
                        return False
            if open_or_cl == 0:
                return True
    return False


msg = input()
print(is_correct_bracket(msg))
