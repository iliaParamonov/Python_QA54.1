import csv
import json


# Task1
print("Task 1")

def save_books(books):
    with open("books.txt", "w", encoding="utf-8") as file:
        for book in books:
            file.write(book + "\n")


books = [
    "Harry Potter",
    "The Hobbit",
    "1984",
    "The Little Prince"
]

save_books(books)
print("Books saved")

# Task2
print("Task 2")

import csv

def read_products(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")


read_products("products.csv")

# Task3
print("Task 3")

import json

print("Task 3")

def save_user(username, email, country):
    user = {
        "username": username,
        "email": email,
        "country": country
    }

    with open("user.json", "w", encoding="utf-8") as file:
        json.dump(user, file, indent=4)


save_user("KpyTou_IIepeZ", "ma@mail.com", "Israel")