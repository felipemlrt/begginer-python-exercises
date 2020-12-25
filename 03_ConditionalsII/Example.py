login = "root"
password = "S4fet1"
user_login = input("What is your login?")
user_password = input("What is your password?")
if login == user_login and password == user_password:
 print("Login sucessful!")
else:
 print("Login failed. Check your login/password")

if login == user_login and password == user_password:
 print("Login sucessful!")
elif login == user_login and password != user_password:
 print("Login failed. Check your password")
elif login != user_login and password == user_password:
 print("Login failed. Check your login")
elif login != user_login and password != user_password:
 print("Login failed. Check your login and password")
else:
 print("ERROR: something unexpected happened!")
