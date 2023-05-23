# Перше завдання
print("1.\n")


def hidden_symbols(text1, text2):
    checkText = ""

    for char in text1:
        flag = text2.find(char, 0)
        if flag != -1:
            checkText += char
        else:
            print("No")
            return

    if text1 == checkText:
        print("Yes")


text1 = "dog"
text2 = "vcxzxduybfdsobywuefgas"

hidden_symbols(text1, text2)

text1 = "dog"
text2 = "vcxzxdcybfdstbywuefsas"

hidden_symbols(text1, text2)


# Друге завдання
print("\n2.\n")


def numberOfLife(date):
    while True:
        date = str(date)
        sum = 0
        for simbol in date:
            sum += int(simbol)

        date = str(sum)

        if len(date) == 1:
            break

    print(sum)


while True:
    try:
        date = int(input("Введіть дату народження у форматі YYYYMMDD:"))
        numberOfLife(date)
        break

    except ValueError:
        print("неприпустимі значення, спробуйте ще раз")


# Третє завдання
print("\n3.\n")


def integer_check(number, min_number, max_number):
    while True:
        flagA = 0
        flagB = 0

        try:
            min_number = int(min_number)
            flagA = 1
        except ValueError:
            print("Error: wrong input for min")
            min_number = input("enter again: ")

        try:
            max_number = int(max_number)
            flagB = 1
        except ValueError:
            print("Error: wrong input for max")
            max_number = input("enter again: ")

        if flagA == 1 and flagB == 1:
            try:
                number = int(number)
                if number >= min_number and number <= max_number:
                    print(number)
                    return
                else:
                    print("Error: the value is not within permitted range (" + str(min_number) + "..." + str(
                        max_number) + ")")
                    number = input("enter again: ")

            except ValueError:
                print("Error: wrong input")
                number = input("enter again: ")


number = input("Enter the number: ")
min_number = input("Enter min_number: ")
max_number = input("Enter max_number: ")

integer_check(number, min_number, max_number)