
# Task 1
def get_product(products, index):
    try:
        return products[index]
    except IndexError:
        return "Product index is out of range"

products = ["coffee", "tea", "milk"]

print("Task 1")
print(get_product(products, 0))
print(get_product(products, 7))

# Task 2
def get_settings_value(settings, key):
    try:
        return settings[key]
    except KeyError:
        return "Setting was not found"

settings = {
    "language": "English",
    "theme": "dark"
}

print("\nTask 2")
print(get_settings_value(settings, "theme"))
print(get_settings_value(settings, "font"))

# Task 3
def calculate_total_price(price, quantity):
    try:
        return float(price) * float(quantity)
    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"

print("\nTask 3")
print(calculate_total_price("12.5", "4"))
print(calculate_total_price("coffee", "4"))
print(calculate_total_price(None, 4))

# Task 4
def read_temperature():
    try:
        temperature = float(input("Enter temperature: "))
        print("Temperature was entered successfully")
    except ValueError:
        print("Invalid temperature")
    finally:
        print("Program finished")

print("\nTask 4")
read_temperature()

# Task 5
def validate_discount(discount):
    if discount < 0:
        raise ValueError("Discount cannot be negative")
    if discount > 100:
        raise ValueError("Discount cannot be greater than 100")
    return discount

print("\nTask 5")
print(validate_discount(50))

try:
    print(validate_discount(-10))
except ValueError as e:
    print(e)

try:
    print(validate_discount(150))
except ValueError as e:
    print(e)

