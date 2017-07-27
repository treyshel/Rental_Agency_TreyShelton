import core, disk

def greeting_message(inventory):
    message = '\t!!Welcome to Trey\'s Dos Wheel Motorcycle Rental Agency!!\n\t\t\t**139.99 each day**\n\t\t\t     **7% tax**\n\t\t\t **10% damage fee**\n\t\t No damage? Get your damage fee back!\n\nType the code of the motorcycle\nyou would like to rent:\n\n'
    for motorcycle in inventory.values():
        message += ('{} -> {} ({})\n'.format(motorcycle.get('code'), motorcycle.get('type_of_motorcycle'), motorcycle.get('color')))
    message += 'Leave program = "Q" + "Enter"\n'
    return message

def get_motorcycle(inventory):
    message = greeting_message(inventory)
    while True:
        choice = input(message)
        if choice.isalpha() == 'Q':
            print('You have left the program.')
            exit()
        else:
            print('---System Error--- ::\\ INVALID CHOICE\n')

def get_days_message(code):
    return '\nYou have chosen the {} rental motorcycle. How many\ndays would you like to rent this bike?'.format(code)







def main():
    read_line, read_lines = disk.dos_inventory()
    inventory = core.inventory(read_line, read_lines)
    type_motorcycle = get_motorcycle(inventory)
    
    
    





    
if __name__ == '__main__':
    main()

