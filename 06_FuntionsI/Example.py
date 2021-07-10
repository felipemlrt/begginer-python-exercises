def sum_all(list_of_numbers):
 """Returns the total sum of a given list of numbers.
 """
 total = 0
 for number in list_of_numbers:
  total = total + list_of_numbers[number]
 return total

 def login(user_login, user_password):
  """For example only! Do not use for real appplication, this is not secure enough.
  """
  login, password = 'John', 'Pa55Word'
  if user_login == login and user_password == password:
   return True
  else:
   return False
