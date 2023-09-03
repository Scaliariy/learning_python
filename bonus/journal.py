date = input("Enter today`s date: ")
mood = input("How do you rate your mood today's from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

mood = f"Rating of the day: {mood}" + 2 * '\n'
date = date.replace('.', '-')

with open(f"journal/{date}.txt", 'w') as file:
    day = [mood, thoughts]
    file.writelines(day)
