def sum_all(list_of_numbers):
 total = 0
 for number in list_of_numbers:
  total = total + list_of_numbers[number]
 return total

 def login(user_login, user_password):
  login, password = 'John', 'Pa55Word'
  if user_login == login and user_password == password:
   return True
  else:
   return False
