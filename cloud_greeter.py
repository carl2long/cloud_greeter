import datetime

name = input("Enter your name: ")
color = input("What's your favorite color? ")

now = datetime.datetime.now()

greeting  = (
    f"Hello {name}! Today is {now:%A, %B %d, %Y}.\n"
    f"Your favorite color is {color}."
)

print(greeting)

with open("greeting.txt", "w") as f:
    f.write(greeting)

print("\nGreeting saved to greeting.txt")
