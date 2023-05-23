# Перше завдання
print("1.\n")

text = input("Enter your message: ")
step = int(input("Enter your step: "))
flag = 0

while flag == 0:
    if step < 1 or step > 25:
        print("valve worst!!! need 1 - 25")
        step = int(input("Enter your step: "))
    else:
        flag = 1

cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue

    if char.isupper():
        char_value = ord(char) + step
        if char_value > ord("Z"):
            char_value = char_value - ord("Z")
            char_value = ord("A") + char_value - 1
            cipher += chr(char_value)
            continue
        cipher += chr(char_value)
    else:
        char_value = ord(char) + step
        if char_value > ord("z"):
            char_value = char_value - ord("z")
            char_value = ord("a") + char_value - 1
            cipher += chr(char_value)
            continue
        cipher += chr(char_value)

print(cipher)