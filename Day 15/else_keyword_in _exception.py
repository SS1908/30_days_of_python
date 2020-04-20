"""
    You can use the " else " keyword to define a block of code to be executed if no errors were raised

"""

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")