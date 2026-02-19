username = input("enter username: ")
password = input("enter password: ")
if(username == "admin" and password == "pass"):
    print("LOGIN Sucessful!")
elif(username != "admin"):
    print("Wrong Username")
else:
    print("Wrong Password!")
