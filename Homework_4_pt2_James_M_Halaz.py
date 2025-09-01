### Homework 4 part 2
### James M. Halaz

## Question 15
import datetime
Present = datetime.datetime.now()
current_m = Present.strftime("%B")
print(current_m)

## Question 16
def greetings(first_name, day_name="Sunday"):
    print(f"Hi {first_name}! Today is {day_name}.")

greetings("Mikey", "Thursday")
greetings("Sakura")

## Question 17
color_list = ["aqua", "teal", "azure", "crimson"]
color_num = int(input("Select a color number: "))
try:
    print("Your color is", color_list[color_num])
except IndexError:
    print("I have not come up with a color for that number.")
else:
    print(f"{color_list[color_num]} is a nice color")
finally:
    print("Do your want to help me come up with more colors for numbers")