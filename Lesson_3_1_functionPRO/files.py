def log_res(test_name,status):
    with open("test_1.txt","a",encoding="utf-8") as file:
        file.write(f"{test_name}: {status}\n")
log_res("test_register","PASSED")
log_res("test_login","FAILED")
log_res("test_logout","PASSED")