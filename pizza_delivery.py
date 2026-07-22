print("welcome to python pizza deliveries!")



size = input("what size of pizza would you like? S, M or L: ").upper()

pepperoni = input("do you want pepperoni on your pizza? Y or N: ").upper()

extra_cheese = input("do you want extra cheese on your pizza? Y or N: ").upper()

bill = 0

if size == "S":
  bill += 15

elif size == "M":
  bill += 20

elif size == "L":
  bill += 25


if pepperoni == "Y":
  if size == "S":
    bill += 2
  
  else:
    bill += 3


if extra_cheese == "Y":
  bill += 1

print(f"your final bill is ${bill}")


  