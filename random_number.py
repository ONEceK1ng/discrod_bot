import random

random_number = random.randint(1, 50)

# print(random_number)
tries = 0


while tries < 6:
    user = int(input("Vvedi chislo - "))

    tries += 1 

    if user < random_number:
        print("Your number << random_number")
    if user > random_number:
        print("Your number >> random_number")
    if user == random_number:
        print(f"Nice, your tries {tries}")
        break
    if user != random_number and tries == 6:
        print(f"6 tries, loh, chislo bula : {random_number}")
        break



