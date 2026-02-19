username = input("enter username: ")
password = input("enter password: ")
if(username == "admin" and password == "pass"):
    print("LOGIN Sucessful!")
else:
    if(username != "admin"):
        print("Wrong Username")
    else:
        print("Wrong Password!")