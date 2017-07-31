from core import *
from disk import *
import time

def greeting_message(inventory):
    message = '\t!!Welcome to Trey\'s Dos Wheel Motorcycle Rental Agency!!\n\n\n\t\t\t**139.99 each day**\n\t\t\t     **7% tax**\n\t  **3 FREE DAYS IF PURCHASED FOR 28 DAYS OR MORE**\n\t\t **10% damage fee added to price**\n\t\t No damage? Get your damage fee back!\n\nType the code of the motorcycle\nyou would like to rent:\n\n'
    for motorcycle in inventory.values():
        message += ('{} -> {} ({}): ${}\n'.format(motorcycle.get('code'), motorcycle.get('type_of_motorcycle'), motorcycle.get('color'), motorcycle.get('price')))
    message += 'Leave program = "Q" + "Enter"\n\n'
    code = input(message)
    return code

def get_motorcycle(inventory):
    while True:
        choice = greeting_message(inventory)
        if choice == 'Q':
            print('You have left the program.')
            exit()
        elif choice in inventory.keys():
            return choice
        else:
            print('---System Error--- :INVALID:/..CHOICE:/\n')

def get_days_message(type_of_motorcycle,inventory,choice):
    days = int(input('\nThe {} rental motorcycle is ${} before the 10%\ndamage fee. How many days would you like to rent this bike?\n'.format(type_of_motorcycle, inventory[choice]['price'])))
    return days

def name_for_return():
    name = str(input('\nAnd what will be the name you would like your Dos Motorcycle\norder to be under?\n'))
    return name

def return_message(type_of_motorcycle, name, total):
    print('\nName: {}\nYour Dos Motorcycle: {}\nTaxes: 7% of days (139.99/day)\nDamage Deposit: 10% of Motorcycle Cost\nYour total will be ${}'.format(name, type_of_motorcycle, total))

def return_day(type_of_motorcycle, name, deposit):
    input('Hello! We hope you had a great experience with our Dos\nMotorcycle! What was the name for your rental under?\n')
    # if name == name_for_return():
    #     print('Okay, it looks like you rented the {}. Here is your return\ndeposit of ${}, have a great day!'.format(type_of_motorcycle, deposit))
    # else:
    #     input('I\'m sorry but we don\'t have a {}. Are there any\n other names you think it would maybe be under?\n')


def main():
    i, inv = dos_inventory()
    in_inventory = motorcycle_inventory(i, inv)
    type_of_motorcycle = get_motorcycle(in_inventory)
    pick = choose_motorcycle(in_inventory, type_of_motorcycle)
    days = get_days_message(pick, in_inventory,type_of_motorcycle)
    name = name_for_return()
    deposit = damage_deposit(type_of_motorcycle, in_inventory)
    amount = adding_tax(days)
    total = damage_deposit_and_tax(deposit, amount)
    return_message(type_of_motorcycle, name, total)
    quantity_take_away(in_inventory, type_of_motorcycle)
    in_history(name, type_of_motorcycle, days, total)
    print('----------------------------------------------------------------------------------\n\n*RETURN DAY*\n\n\n')
    return_day(type_of_motorcycle, name, deposit)


    
    
    



    
if __name__ == '__main__':
    main()

