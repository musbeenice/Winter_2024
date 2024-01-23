# Третья задача к третьему занятию

# several longest words are shown:

# message = input()
# lst_msg = message.split()

# longest_words = []
# max_length = 0

# for word in lst_msg:
#     if len(word) > max_length:
#         max_length = len(word)
# for word in lst_msg:
#     if max_length == len(word):
#         longest_words.append(word)
# print(" ".join(longest_words))

# or

# s = input().split()
# ma = ""
# for w in s:
#     if len(w) > len(ma):
#         ma = w
# for w in s:
#     if len(w) == len(ma):
#         print(w)

# or

s = input().split()
res = [""]
for w in s:
    if len(w) == len(res[0]):
        res.append(w)
    elif len(w) < len(res[0]):
        continue  # 'pass' работает по-другому
    elif len(w) > len(res[0]):
        res = [w]
    print(*res)
print(*res)  # распечатывает список

# only the first longest word encountered is shown:

# message = input()
# lst_msg = message.split()

# longest_word = lst_msg[0]

# for word in lst_msg:
#     if len(word) > len(longest_word):
#         longest_word = word
# print("".join(longest_word))
