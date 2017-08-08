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


def get_days_message(type_of_motorcycle, inventory, choice):
    while True:
        days = input(
            '\nThe {} rental motorcycle is ${} before the 10%\ndamage fee. How many days would you like to rent this bike?\n'.
            format(type_of_motorcycle, inventory[choice]['price']))
        if days.strip().isnumeric():
            return days
        else:
            print('\nINVALID CHOICE')


def return_message(pick, total):
    print(
        '\nYour Dos Motorcycle: {}\nTaxes: 7% of days ($139.99/day)\nDamage Deposit: 10% of Motorcycle Cost\nYour total will be ${:.2f}\n\nHAVE A GREAT DAY!'.
        format(pick, total))


def customer_chooses_bike_they_rented(inventory):
    message = '\nWe hope you had a great experience with our Dos\nMotorcycle!\nPlease choose the motorcycle that you rented from us:\n\n'
    for motorcycle in inventory.values():
        message += ('{} -> {} ${}\n'.format(
            motorcycle.get('code'),
            motorcycle.get('type_of_motorcycle'), motorcycle.get('price')))
    message += 'OR type "Q" to leave the program\n\n'
    return message


def return_amount_of_days(choice):
    while True:
        days = input('\nHow many days did you have the {}?\n'.format(choice))
        if days.strip().isnumeric():
            return days
        else:
            print('\nINVALID CHOICE. MUST USE A NUMBER.')


def get_return_deposit(motorcycle, days, return_dep):
    print(
        '\nMotorcycle rented: {}\nAmount of days rented: {}\nReturn deposit: ${}'.
        format(motorcycle, days, return_dep))


def customer_decision():
    while True:
        decision = input(
            '\nHey there! What will you be needing today?\n\n*Press 1 to rent a Dos Wheel Motorcycle\n*Press 2 to return a Dos Wheel Motorcycle\n'
        )
        if decision == '1':
            i, inv = dos_inventory()
            in_inventory = motorcycle_inventory(i, inv)
            greeting_message = get_greeting_message(in_inventory)
            code = get_motorcycle(in_inventory, greeting_message)
            pick = choose_motorcycle(in_inventory, code)
            days = get_days_message(pick, in_inventory, code)
            deposit = damage_deposit(code, in_inventory)
            amount = adding_tax(int(days))
            total = damage_deposit_and_tax(deposit, amount)
            return_message(pick, total)
            quantity_take_away(in_inventory, code)
            in_history(code, days, total)
            break
        elif decision == '2':
            return_i, return_inv = dos_inventory()
            return_in_inventory = motorcycle_inventory(return_i, return_inv)
            return_greeting_message = customer_chooses_bike_they_rented(
                return_in_inventory)
            return_code = get_motorcycle(return_in_inventory,
                                         return_greeting_message)
            return_pick = choose_motorcycle(return_in_inventory, return_code)
            return_days = return_amount_of_days(return_pick)
            return_deposit = damage_deposit(return_code, return_in_inventory)
            get_return_deposit(return_pick, return_days, return_deposit)
            quantity_after_return(return_in_inventory, return_code)
            history_for_return(return_code, return_days, return_deposit)
            break

        else:
            print(
                'I\'m sorry. You have chosen an invalid decision.\nPlease try again.'
            )


def main():
    while True:
        customer_or_employee = input('Are you a customer or an employee?\n')
        if customer_or_employee.title().strip() == 'customer'.title().strip():
            return customer_decision()
        else:
            print('Please type customer or employee to continue.\n')


if __name__ == '__main__':
    main()
