# Третья задача к двадцать четвертому занятию

# def is_correct_bracket(text):
#     if "(" in text and ")" in text and not text.isalnum():
#         open_or_cl = 0
#         if not text.startswith(")") and not text.endswith("("):
#             for char in text:
#                 if char == "(":
#                     open_or_cl += 1
#                 elif char == ")":
#                     open_or_cl -= 1
#                     if open_or_cl < 0:
#                         return False
#             if open_or_cl == 0:
#                 return True
#     return False
#
#
# msg = input()
# print(is_correct_bracket(msg))

# or


# def parenthesis(s):
#     count = 0
#     for i in s:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -= 1
#         else:
#             return False
#         if count < 0:
#             return False
#     if count == 0:
#         return True
#     return False
#
#
# print(parenthesis(input()))

# or


# def valid_parenthesis(s):
#     while "()" in s:
#         s = s.replace("()", "")
#         print(s)
#     return s == ""
#
#
# print(valid_parenthesis(input()))

# or


def braces(s):
    d = {"(": 1, ")": -1}
    r = 0
    for i in s:
        r += d[i]
        print(r)
        if r < 0:
            return False
    return r == 0


print(braces(input()))
