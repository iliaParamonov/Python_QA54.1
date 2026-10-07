with open("user.txt","w",encoding="utf-8") as file:
    file.write("Kristina\n")
    file.write("Alex\n ")

    #read()- весь файл полностью
with open("user.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(len(content))