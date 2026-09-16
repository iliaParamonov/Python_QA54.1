
#Task №1
print("Task №1")
def clean_name(name):
    return name.strip().title()

print(clean_name("   Paramonov Ilia"        ))
print(clean_name("Ivan Pelmen"))
print("")

#Task №2
print("Task №2")
def normalize_email(email):
    return email.strip().lower()

print(normalize_email(" margo.borsch@Example.COM "))
print(normalize_email(" USER123@GMAIL.COM "))
print("")

#Task №3
print("Task №3")
def is_python_file(filename):
    return filename.lower().endswith(".py")

print(is_python_file("homework.PY"))
print(is_python_file("photo.jpg"))
print("")

#Task №4
print("Task №4")
def fix_message(message):
    return message.replace("bad", "good")

print(fix_message("bad day, bad weather"))
print(fix_message("this is a bad idea"))
print("")

#Task №5
print("#Task №5")
def count_letter(text, letter):
    return text.lower().count(letter.lower())

print(count_letter("Hello World", "l"))
print(count_letter("676767676767676767", "67"))
print("")

#Task №6
print("#Task №6")
def create_login(first_name, last_name):
    f = first_name.strip().lower()
    l = last_name.strip().lower()

    return f + "." + l + "@something.com"

print(create_login(" Ilya ", " PARAMONOV "))
print(create_login(" Elena ", " GOLOWACH "))
print("")

#Bonus №1
print("Bonus №1")
def split_name(full_name):
    return full_name.strip().split()

print(split_name("Paramonov Ilia"))
print(split_name("Lavin Yasha"))

#Bonus №2
print("Bonus №2")

def check_password(password):
    return len(password) >= 8 and " " not in password and not password.isalpha()

print(check_password("qwerty"))
print(check_password("oguretc13"))