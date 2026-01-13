print("1. Register\n2. Login\n3. Exit")
user_input=int(input("Enter your choice: "))
print(f"You selected: {user_input}")

with open("users.txt","a") as f:
    user_name=f.write(input("Enter your user name: "))
    password=f.write(input("Enter your password: "))