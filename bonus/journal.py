import time

now = time.strftime("%d-%m-%Y")

# date = input("Enter today`s date: ")
date = now
mood = input("How do you rate your mood today's from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

mood = f"Rating of the day: {mood}" + 2 * '\n'

with open(f"journal/{date}.txt", 'w') as file:
    day = [mood, thoughts]
    file.writelines(day)
