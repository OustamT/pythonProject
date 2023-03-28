# Перше завдання
print("1.\n")

hat_list = [1, 2, 3, 4, 5]

center_number = int(input("Введіть бажане число замість початкового середнього: "))

hat_list[2] = center_number
print(hat_list)

del hat_list[-1]
print("\n""результат видалення останнього елемента масиву: ", hat_list)

print("\n""довжина існуючого списку: ", len(hat_list))

# Друге завдання
print("\n2.\n")

array_list = []

for i in range(int(input("Введіть розмір масиву: "))):
    array_list.append(int(input("введіть значення елемента масиву: ")))

print("\n""зовнішній вигляд створеного масиву: ", array_list)

last_value = len(array_list) - 1

while last_value > 0:
    fresh_value = 0
    for i in range(last_value):
        if array_list[i] > array_list[i + 1]:
            array_list[i], array_list[i + 1] = array_list[i + 1], array_list[i]
            fresh_value = i
    last_value = fresh_value

print("\n""відсортований масив: ", array_list)

# Третє завдання
print("\n3.\n")

fixed_list = []
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in my_list:
    if i not in fixed_list:
        fixed_list.append(i)

print("The list with unique elements only:")
print(my_list)
print("\n""результат після видалення повторів: ""\n", fixed_list)

# Четверте завдання
print("\n4.\n")

chess_field = [['_' for i in range(8)] for j in range(8)]

chess_field[0][0] = "♜"
chess_field[0][7] = "♜"
chess_field[7][0] = "♜"
chess_field[7][7] = "♜"

x = 0
while x < 8:
    print(chess_field[x])
    x += 1
