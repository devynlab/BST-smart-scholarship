from datetime import date


def calculate_age():
  date_of_birth_1 = date(1998, 3, 8)
  date_of_birth_2 = date(1999, 6, 1)
  today = date.today()
  age_1 = today - date_of_birth_1
  age_2 = today - date_of_birth_2
  print(age_1)
  print(age_2)
  print("=====Age Difference=====")
  print(age_1-age_2)
  if age_1 > age_2:
    print('Age 1 is older than Age 2')


calculate_age()
