words = []
try:
    while True:
        word = input()
        if word == " ":
            break
        elif word not in words:
            words.append(word)
except EOFError:
    pass

for word in words:
    print(word)
