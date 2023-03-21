# Перше завдання
print("1.\n")

n = int(input("Введіть змінну n: "))

print(n < 100)

# Друге завдання
print("\n2.\n")

first_number = float(input("Введіть перше число: "))
second_number = float(input("Введіть друге число: "))

if first_number > second_number:
    print(first_number, "більше", second_number)
else:
    print(second_number, "більше", first_number)

# Третє завдання
print("\n3.\n")

plant_container = input("Enter plant name:")

if plant_container == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant_container == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", plant_container + "!")

# Четверте завдання
print("\n4.\n")

income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)

if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# П'яте завдання
print("\n5.\n")

year = int(input("Введіть рік: "))

if year < 1582:
    print("Not within the Gregorion calendar period")
elif year % 4:
    print("Common year")
elif year % 100:
    print("Leep year")
elif year % 400:
    print("Common year")
else:
    print("leap year")

# Шосте завдання
print("\n6.\n")

secret_number = 777

print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Введіть ціле число:"))

while user_number != secret_number:
    print("Ха-ха! Ви застрягли у моїй петлі!")
    user_number = int(input("ввести число знову:"))
else:
    print("Молодець, магле! Тепер ти вільний")

# Сьоме завдання
print("\n7.\n")

import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

# Восьме завдання
print("\n8.\n")

while True:
    word = input("Введіть слово: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break

# Дев'яте завдання
print("\n9.\n")

user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "A, E, I, O, U":
        continue

    print(letter)

# Десяте завдання
print("\n10.\n")

word_without_vowels = ""
user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "A, E, I, O, U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)

# Одинадцяте завдання
print("\n11.\n")

number = int(input("Введіть кількість блоків для  "))

height = 0
blocks = 1

while number > blocks:
    height += 1
    number -= blocks
    blocks += 1

print("The height of the pyramid:", height)

# Дванадцяте завдання
print("\n12.\n")

c = int(input("Введіть натуральне число для c0:"))
steps = 0

while c != 1:
    if c % 2 == 0:
        c = c // 2
        print(c)
    else:
        c = 3 * c + 1
        print(c)
    steps += 1
print("steps = ", steps)
