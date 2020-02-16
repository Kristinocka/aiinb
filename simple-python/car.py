import random


class Car:

    def __init__(self, year, model, tank_condition=50, tank_capacity=50):
        self.year = year
        self.model = model
        self.mileage = 0
        self.tank_capacity = tank_capacity
        self.tank_condition = tank_condition
        # self.fuel_consumption = random.randint(5, 10)
        self.fuel_consumption = 10

    def __repr__(self):
        return f'Your car: \n Model: {self.model} \n Year: {self.year} \n Mileage: {self.mileage}km \n Fuel consuption: {self.fuel_consumption}'

    def drive(self, miles):
        self.mileage += miles
        fuel_used = (self.fuel_consumption * miles) / 100
        self.tank_condition -= fuel_used
        if (self.tank_condition <= 0):
            print(
                f'Heeeey.. you cannot drive any more. Your tank condition is {self.tank_condition} :( You\'ve driven already {self.mileage}')
        else:
            print(f'You\'ve used {fuel_used} fuel. There is only {self.tank_condition} of fuel left')

    def refuel(self, amount_of_fuel):
        if (self.tank_capacity >= self.tank_condition + amount_of_fuel):
            self.tank_condition += amount_of_fuel
            print(
                f'You\'ve successfully refueled your car for {amount_of_fuel} litres. Now you have {self.tank_condition} litres of fuel')
        else:
            print(
                f'You cannot refuel so much.. Your max tank capacity is  {self.tank_capacity} litres of fuel. Now you have {self.tank_condition}')

#
# my_car = Car(2008, 'audi', 50)
# print(my_car)
# my_car.drive(100)
# my_car.drive(200)
# my_car.drive(200)
# my_car.refuel(50)
#

# print(my_car)

# Audi 2008 2.0 tdi

def user_interaction():
    user_info = input(
        'Please provide main info regarding your car: year, model, tank condition*, tank_capacity*. \n *by default = 50 \n');
    print(user_info)
    splited = user_info.split(',')
    print(splited)
    user_car = Car(*splited)
# user_interaction()


def ask_user(message='', type=str):
    user_input = ''
    while not user_input:
        try:
            user_input = type(input(message).strip())
        except ValueError:
            continue
    return user_input


def complete_form():
    return Car(ask_user("Enter Car Year: ", type=int),
                 ask_user("Enter Car Model: ").title(),
                 ask_user("Enter Tank Condition: ", type=int))

auto_rafala = complete_form()

auto_rafala.drive(100)