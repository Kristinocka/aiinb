import random as rd
#my_choice = 40
my_choice = rd.randint(0, 100)


user_choice = input("Your first shot: ")
while not(user_choice.isnumeric()):
    user_choice = input("Your second shot: ")


while int(user_choice) != my_choice:
        user_choice = int(user_choice)
        print(f"No... please try more than {user_choice}") if user_choice < my_choice else print(f"No... please try less than {user_choice}")
        user_choice = int(input("provide your choice: "))

        print(f"You're right! My choice was {my_choice}") if user_choice == my_choice else print("")
