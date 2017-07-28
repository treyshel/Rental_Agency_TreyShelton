from core import *
from disk import *
import time

def greeting_message(inventory):
    message = '\t!!Welcome to Trey\'s Dos Wheel Motorcycle Rental Agency!!\n\t\t\t**139.99 each day**\n\t\t\t     **7% tax**\n\t\t **10% damage fee added to price**\n\t\t No damage? Get your damage fee back!\n\nType the code of the motorcycle\nyou would like to rent:\n\n'
    for motorcycle in inventory.values():
        message += ('{} -> {} ({}): ${}\n'.format(motorcycle.get('code'), motorcycle.get('type_of_motorcycle'), motorcycle.get('color'), motorcycle.get('price')))
    message += '\nLeave program = "Q" + "Enter"\n\n'
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
            print('---System Error--- ::\\ INVALID CHOICE\n')

def get_days_message(type_of_motorcycle,inventory,choice):
    input('\nThe {} rental motorcycle is ${} before the 10%\ndamage fee. How many days would you like to rent this bike?\n'.format(type_of_motorcycle, inventory[choice]['price']))

def return_message():
    print('Your total, after taxes and damage fees, will be {}.'.format())

def main():
    i, inv = dos_inventory()
    in_inventory = motorcycle_inventory(i, inv)
    type_of_motorcycle = get_motorcycle(in_inventory)
    pick = choose_motorcycle(in_inventory, type_of_motorcycle)
    days = get_days_message(pick, in_inventory,type_of_motorcycle)
    deposit = damage_deposit(type_of_motorcycle, in_inventory)
    amount = adding_tax(days)
    total = damage_deposit_and_tax(deposit, amount)
    



    
    
    



    
if __name__ == '__main__':
    main()

