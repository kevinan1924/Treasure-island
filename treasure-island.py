print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = (input("Left or Right?\n"))
direction = direction.lower()
if direction != "left":
  print("Fall into a hole. You died.\n")
elif direction == "left":
  choice = input("Swim or wait?\n")
  choice = choice.lower()
  if choice != "wait":
    print("Attacked by shark. You died.\n")
  elif choice == "wait":
    door_one = input("Which door?\n")
    door_one = door_one.lower()
    if door_one == "red":
      print("Burned by fire. You died.")
    elif door_one == "blue":
      print("Eaten by beasts. You died.")
    elif door_one == "yellow":
      print("You win!")
    else:
      print("Game over.")
