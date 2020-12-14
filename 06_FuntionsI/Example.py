def sum_all(list_of_numbers):
 total = 0
 for number in list_of_numbers:
  total = total + list_of_numbers[number]
 return total

def test_value(value, test_value):
 if value == test_value:
  return True
 else:
  return False
