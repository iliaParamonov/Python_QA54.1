# Task 1
print("Task 1")
def clean_cart(cart):
    i = 0

    while i < len(cart):
        if cart[i] == "sold out":
            cart.pop(i)
        else:
            i += 1

    return cart


print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))


# Task 2
print("Task 2")
def temperature_report(temperatures):
    result = []

    for temperature in temperatures:
        if temperature > 25:
            result.append(temperature)

    return result


print(temperature_report([21, 28, 19, 31, 25, 27]))


# Task 3
print("Task 3")
def fix_balances(balances):
    for i in range(len(balances)):
        if balances[i] < 0:
            balances[i] = 0

    return balances


print(fix_balances([120, -30, 50, -5, 0, 200]))


# Task 4
print("Task 4")
def unique_items(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


print(unique_items(["red", "blue", "red", "green", "blue"]))


# Task 5
print("Task 5")
def longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(longest_word(["cat", "elephant", "python", "coffee"]))