# Ethan Mayer
# Feb 17, 2026

health = 100

while health > 0:
    print(f"Your health is {health}.")
    damage = int(input("Enter the damage taken: "))
    health -= damage

    print("Game Over!")

