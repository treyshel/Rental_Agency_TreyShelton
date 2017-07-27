import core, disk

def greeting_message(inventory):
    message = '\t!!Welcome to Trey\'s Dos Wheel Motorcycle Rental Agency!!\n\t\t\t**139.99 each day**\n\t\t\t     **7% tax**\n\t\t\t **10% damage fee**\n\t\t No damage? Get your damage fee back!\n\nChoose the type of motorcycle you would like to rent:\n'
    for motorcycle in inventory.values():
        message += ('{}. -> {} ({})\n'.format(motorcycle.get('code'), motorcycle.get('type_of_motorcycle'), motorcycle.get('color')))
    message += 'Leave program = "Q" + "Enter"\n'
    return message

def get_amount_of_days(inventory):
    message = greeting_message(inventory)
    while True:
        choice = input(message)
        if choice.isalpha() == 'Q':
            print('You have left the program.')
            exit()
        else:
            input('---System Error--- ::\\ INVALID CHOICE')







def main():
    keys, lines = disk.dos_inventory('inventory.txt')
    inventory = core.inventory(keys, lines)
    days = get_amount_of_days(inventory)
    
    





    
if __name__ == '__main__':
    main()

