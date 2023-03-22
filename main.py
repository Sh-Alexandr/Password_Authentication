import getpass
database = {"Alex": "123456", "Cat": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass(prompt='Enter Your Password: ', stream=None)
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")