# Перше завдання
print("1.\n")

list_input = input("Введіть числа, розділені комою: ").split(',')
n = int(input("введіть число n:"))
numbers = []

for number in list_input:
    number = int(number)
    numbers.append(number)

tuple_numbers = tuple(numbers)

result = [i for i in tuple_numbers if i < n]
result = sorted(result)

print("числа, які менші від заданого числа n: ", end=" ")
for i in result:
    print(i, end=" ")
print()

# Друге завдання
print("\n2.\n")

print("Введіть значення для трьох елементів котеджу")

first_str = input("перший елемент: ")
second_str = input("другий елемент: ")
third_str = input("третій елемент: ")

tuple_str = (first_str, second_str, third_str)
join_str = ', '.join(tuple_str)
print(join_str)

# Третє завдання
print("\n3.\n")

book_library = {
                "Хрещений батько": "Маріо Пьюзо, опубліковано у 1969 році, 288 сторінок. ",
                "Володар кілець": "Джон Рональд Руэл Толкин,  опубліковано у 1954 році, 1408 сторінок.",
                "1984": "Джордж Орвелл, опубліковано у  1949 році, 312 сторінок."
}

user_input = input("Введіть назву книги: ")
if user_input in book_library:
    print(user_input, "-", book_library[user_input])
else:
    print(user_input, "немає в бібліотеці словника")

# Четверте завдання
print("\n4.\n")

students_info = {}

while True:
    last_name = input("Введіть прізвище студента, щоб створити новий список, або натисніть клавішу Enter, щоб вийти: ")
    if last_name == '':
        break

    elif last_name in students_info:
        print("цього студента вже введено в словник")
    else:
        info = input("введіть інформацію про студента: ")
        students_info[last_name] = (info,)

lname_input = input("\nВведіть прізвище студента, щоб дізнатися його інформацію: ")
if lname_input in students_info:
    print(lname_input + ":", students_info[lname_input][0])
else:
    print(lname_input, "немає у словнику")

# П'яте завдання
print("\n5.\n")

contact_list = {
    "Сем": ["+38045...", "+380534...", "+380565..."],
    "Том": ["+38088...", "+380322..."],
    "Боб": ["+380053...", "+380032...", "+380232..."]
}


def new_number(contact_name, phone_number):
    if contact_name in contact_list:
        if phone_number not in contact_list[contact_name]:
            contact_list[contact_name].append(phone_number)
        else:
            print("номер", phone_number, "вже є в списку")
    else:
        print("не знайдено контакт з іменем", contact_name, " ")


new_number("Роб", "+38033..")
new_number("Сем", "+38045...")
new_number("Том", "+380543...")

print("\n" + "Список усіх контактів:")
for contact_name, phone_numbers in contact_list.items():
    print(contact_name + ":", contact_list[contact_name])
