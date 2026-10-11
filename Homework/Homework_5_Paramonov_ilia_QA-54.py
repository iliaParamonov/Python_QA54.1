# Task 1
print("Task 1")
def save_test_ids(test_ids):
    with open("tests.txt", "w") as file:
        for test_id in test_ids:
            file.write(test_id + "\n")

def add_test_id(test_id):
    with open("tests.txt", "a") as file:
        file.write(test_id + "\n")

def load_test_ids(filename):
    test_ids = []

    with open(filename, "r") as file:
        for line in file:
            test_id = line.strip()
            if test_id:
                test_ids.append(test_id)

    return test_ids

save_test_ids(["QA-1001", "QA-1002", "QA-1003"])
add_test_id("QA-1004")
print(load_test_ids("tests.txt"))

save_test_ids([])
print(load_test_ids("tests.txt"))

save_test_ids(["QA-1001"])
add_test_id("QA-1001")
print(load_test_ids("tests.txt"))

with open("tests.txt", "w") as file:
    file.write("QA-1001\n\n QA-1002 \n\nQA-1003\n")

print(load_test_ids("tests.txt"))
print("")


# Task 2
print("Task 2")
import csv

def get_test_statistics(filename):
    statistics = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "total_duration_ms": 0,
        "failed_ids": []
    }

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            statistics["total"] += 1
            statistics["total_duration_ms"] += int(row["duration_ms"])

            if row["status"] == "PASSED":
                statistics["passed"] += 1

            if row["status"] == "FAILED":
                statistics["failed"] += 1
                statistics["failed_ids"].append(row["test_id"])

    return statistics

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_id", "status", "duration_ms"])
    writer.writerow(["QA-1001", "PASSED", 120])
    writer.writerow(["QA-1002", "FAILED", 230])
    writer.writerow(["QA-1003", "PASSED", 150])

print(get_test_statistics("results.csv"))

# Header only
with open("empty_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_id", "status", "duration_ms"])

print(get_test_statistics("empty_results.csv"))
print("")

# Task 3
print("Task 3")

import json

def save_test_config(environment, base_url, timeout):
    config = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout
    }

    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)


def load_test_config(filename):
    with open(filename, "r") as file:
        config = json.load(file)

    return config

save_test_config("staging", "https://example.com", 30)

config = load_test_config("config.json")
print(config)

assert type(config["timeout"]) == int

# Overwrite old config
save_test_config("production", "https://production.com", 60)

new_config = load_test_config("config.json")
print(new_config)

assert new_config["environment"] == "production"
assert new_config["timeout"] == 60
assert type(new_config["timeout"]) == int
print("")