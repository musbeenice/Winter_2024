# Третья задача к шестнадцатому занятию

def lowercase_deco(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.lower()
        return modified_result
    return wrapper
@lowercase_deco
def f():
    return input("Enter your message:\n")
print(f())
