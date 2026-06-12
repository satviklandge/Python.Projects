import random

name = input("Enter your name: ").strip()

vibes = ["Cool", "Awesome", "Amazing", "Fantastic", "Incredible"]

for i in range(6):
    vibe = random.choice(vibes)
    number = random.randint(1, 100)
    print(f"{name}, your vibe is {vibe}! Number: {number}")
