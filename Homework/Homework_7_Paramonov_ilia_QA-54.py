import re

print("Task 1")

def is_positive_less_than_300(value):
    pattern = r"([1-9]|[1-9]\d|[12]\d{2})"
    return re.fullmatch(pattern, value) is not None


print(is_positive_less_than_300("1"))
print(is_positive_less_than_300("15"))
print(is_positive_less_than_300("299"))
print(is_positive_less_than_300("0"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("-5"))

print("\nTask 2")

def is_number_from_1_to_255(value):
    pattern = r"([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    return re.fullmatch(pattern, value) is not None


print(is_number_from_1_to_255("25"))
print(is_number_from_1_to_255("255"))
print(is_number_from_1_to_255("256"))
print(is_number_from_1_to_255("025"))

print("\nTask 3")

def is_israel_mobile(phone):
    pattern = r"(05\d|\+9725\d)(\d{7}|-\d{7}|-\d{3}-\d{4}|-\d{2}-\d{2}-\d{3})"
    return re.fullmatch(pattern, phone) is not None


print(is_israel_mobile("0541234567"))
print(is_israel_mobile("054-1234567"))
print(is_israel_mobile("+97254-123-4567"))
print(is_israel_mobile("058-12-34-567"))

print(is_israel_mobile("54-1234567"))
print(is_israel_mobile("054--12-4567"))
print(is_israel_mobile("+972054-123-4567"))
print(is_israel_mobile("97254-123-4567"))

print("\nTask 4")

def is_valid_time(time):
    pattern = r"([01]\d|2[0-3]):[0-5]\d"
    return re.fullmatch(pattern, time) is not None


print(is_valid_time("00:00"))
print(is_valid_time("09:30"))
print(is_valid_time("14:45"))
print(is_valid_time("23:59"))

print(is_valid_time("24:00"))
print(is_valid_time("12:60"))
print(is_valid_time("8:30"))
print(is_valid_time("123:45"))
print(is_valid_time("12-30"))
