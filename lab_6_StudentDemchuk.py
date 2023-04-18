# Перше завдання
print("1.\n")


def is_year_leap(year):
    if year < 1582:
        print("Not within the Gregorion calendar period")
        return False
    elif year % 4:
        return False
    elif year % 100:
        return True
    elif year % 400:
        return False
    else:
        return True


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Друге завдання
print("\n2.\n")


def is_year_leap(year):
    if year < 1582:
        print("Not within the Gregorion calendar period")
        return False
    elif year % 4:
        return False
    elif year % 100:
        return True
    elif year % 400:
        return False
    else:
        return True


def days_in_month(year, month):
    array_month = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1582 or month < 1 or month > 12:
        return None
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    else:
        other_months = array_month[month - 1]
        return other_months


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Третє завдання
print("\n3.\n")


def is_year_leap(year):
    if year < 1582:
        print("Not within the Gregorion calendar period")
        return False
    elif year % 4:
        return False
    elif year % 100:
        return True
    elif year % 400:
        return False
    else:
        return True


def days_in_month(year, month):
    array_month = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1582 or month < 1 or month > 12:
        return None
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    else:
        other_months = array_month[month - 1]
        return other_months


def day_of_year(year, month, day):
    if year < 1582 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    else:
        month -= 1
        days = day
        for j in range(0, month):
            days += days_in_month(year, month)
            month -= 1
        return days


print(day_of_year(2000, 12, 31))

# Четверте завдання
print("\n4.\n")


def is_prime(num):
    flag = True
    for x in range(2, num):
        if num % x == 0:
            flag = False
            break
    return flag


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

# П'яте завдання
print("\n5.\n")


def liters_100km_to_miles_gallon(liters):
    miles_of_km = 100 / (1609.344 / 1000)
    liters_100km = liters / 3.785411784
    miles_gallon = miles_of_km / liters_100km
    return miles_gallon


def miles_gallon_to_liters_100km(miles):
    mile_of_km = 1609.344 / 1000
    miles_gallon = (miles * mile_of_km) / 100
    liters_100km = 3.785411784 / miles_gallon
    return liters_100km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# Шосте завдання
print("\n6.\n")


def is_a_triangle(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False


a = float(input("введіть значення для сторони a: "))
b = float(input("введіть значення для сторони b: "))
c = float(input("введіть значення для сторони c: "))

print(is_a_triangle(a, b, c))

# Сьоме завдання
print("\n7.\n")


def is_a_triangle(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False


a = float(input("введіть значення для сторони a: "))
b = float(input("введіть значення для сторони b: "))
c = float(input("введіть значення для сторони c: "))

print(is_a_triangle(a, b, c))


def is_a_right_triangle(a, b, c):
    if (a ** 2) + (b ** 2) == (c ** 2) or (b ** 2) + (c ** 2) == (a ** 2) or (c ** 2) + (a ** 2) == (
            b ** 2) and is_a_triangle(a, b, c):
        return True
    else:
        return False


if is_a_right_triangle(a, b, c):
    print("прямокутний")
else:
    print("не прямокутний")
