from core import *
from disk import *
import time


def get_motorcycle(inventory, message):
    while True:
        code = input(message)
        if code == 'Q':
            print('You have left the program.')
            exit()
        elif code in inventory.keys():
            return code
        else:
            print('---System Error--- :INVALID:/..CHOICE:/\n')

def get_days_message(type_of_motorcycle,inventory,choice):
    while True:
        days = input('\nThe {} rental motorcycle is ${} before the 10%\ndamage fee. How many days would you like to rent this bike?\n'.format(type_of_motorcycle, inventory[choice]['price']))
        if days.strip().isnumeric():
            return days
        else:
            print('\nINVALID CHOICE')

def name_for_return():
    name = str(input('\nAnd what will be the name/code you would like your Dos Motorcycle\norder to be under?\n'))
    return name

def return_message(pick, name, total):
    print('\nName/code: {}\nYour Dos Motorcycle: {}\nTaxes: 7% of days (139.99/day)\nDamage Deposit: 10% of Motorcycle Cost\nYour total will be ${:.2f}'.format(name, pick, total))

def return_day(name, return_name):
    while True:
        if return_name == name:
            print('Okay, it looks like you rented the {}. Here\nis your return deposit of ${:.2f}, have a great day!'.format(pick, deposit))
            break
        else:
            input('\nI\'m sorry but this isn\'t a return name/code. Try again:\n')
            continue

def main():
    i, inv = dos_inventory()
    in_inventory = motorcycle_inventory(i, inv)
    greeting_message = get_greeting_message(in_inventory)
    code = get_motorcycle(in_inventory, greeting_message)
    pick = choose_motorcycle(in_inventory, code)
    days = get_days_message(pick, in_inventory, code)
    name = name_for_return()
    deposit = damage_deposit(code, in_inventory)
    amount = adding_tax(int(days))
    total = damage_deposit_and_tax(deposit, amount)
    return_message(pick, name, total)
    quantity_take_away(in_inventory, code)
    in_history(name, code, days, total)
    print('----------------------------------------------------------------------------------\n\n*RETURN DAY*\n\n\n')
    return_name = input('Hello! We hope you had a great experience with our Dos\nMotorcycle! What was the name for your rental under?\n')
    return_day(name, return_day)
    
    


    
    
    



    
if __name__ == '__main__':
    main()

