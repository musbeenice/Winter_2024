# Третья задача к третьему занятию

# several longest words are shown:

message = input()
lst_msg = message.split()

longest_words = []
max_length = 0

for word in lst_msg:
    if len(word) > max_length:
        max_length = len(word)
for word in lst_msg:
    if max_length == len(word):
        longest_words.append(word)
print(" ".join(longest_words))

# only the first longest word encountered is shown:

# message = input()
# lst_msg = message.split()

# longest_word = lst_msg[0]

# for word in lst_msg:
#     if len(word) > len(longest_word):
#         longest_word = word
# print("".join(longest_word))
