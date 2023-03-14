import math

# Перше завдання
print("1.\n")

print("Введіть значення функцій")

sigma = float(input("\u03C3:"))
x = float(input("x:"))
mu = float(input("\u03BC:"))

fx = (1 / sigma * (2 * math.pi) ** 0.5) * math.exp(-(((x - sigma) ** 2) / (2 * mu ** 2)))

print("Відповідь:", fx)

# Друге завдання
print("\n2.\n")

John = 3
Mary = 5
Adam = 6

print(John, Mary, Adam, sep=",")

total_apples = John + Mary + Adam

print("Загальна кількість яблук:", total_apples)

# Третє завдання
print("\n3.\n")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Четверте завдання
print("\n4.\n")

x = float(input("Введіть значення функцій x:"))
y = (3 * x ** 3) - (2 * x ** 2) + (3 ** x) - 1

print("y =", y)

# П'яте завдання
print("\n5.\n")

# this program computes the number of seconds in a given number of hours

hours = 2
seconds_per_hour = 3600

print("Hours: ", hours)
print("Seconds in Hours: ", hours * seconds_per_hour)

# here we should also print "Goodbye", but a programmer didn't have time to write any code

# Шосте завдання
print("\n6.\n")

# input a float value for variable a here
a = float(input("Введіть значення з плаваючою точкою для змінної a:"))
# input a float value for variable b here
b = float(input("Введіть значення з плаваючою точкою для змінної b:"))

print("\nРезультати арифметичних дій:")
# output the result of addition here
print("1)", a + b, "(додавання);")
# output the result of subtraction here
print("2)", a - b, "(віднімання);")
# output the result of multiplication here
print("3)", a * b, "(множення);")
# output the result of division here
print("4)", a / b, "(ділення).")

print("\nThat's all, folks!")

# Сьоме завдання
print("\n7.\n")

x = float(input("Enter value for x: "))
y = 1 / (x + (1 / (x + (1 / (x + (1 / (x + (1 / x))))))))
print("y =", y)


# Восьме завдання
print("\n8.\n")

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

all_mins_container = hour * 60 + mins + dura
final_hour = (all_mins_container // 60) % 24
final_mins = all_mins_container % 60

print("Result:", final_hour, ":", final_mins)