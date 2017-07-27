# call the inventory.txt file in my parameter when I run this function
def dos_inventory():
    ''' None -> [str, [str, int]]
    [[0660, '2006 Suzuki GSXR 600', 'blue', 5], [0410, '2004 Yamaha R1 1000', 'red', 9], [0190, '2001 Kawasaki Ninja ZX-9R 900', 'grey', 4], [1650, '2016 Honda CBR 500', 'white', 2], [1765, '2017 Kawasaki Ninja EX 650', 'green', 4], [0910, '2009 Suzuki GSX 1000 Hayabusa', 'black', 8]]
    '''
    with open('inventory.txt', 'r') as file:
        read_line = file.readline().strip().split(', ')
        read_lines = file.readlines()
    return [read_line, read_lines]

def open_history():
    ''' [[str ,str, float]] -> None'''
    history = []
    with open('history.txt', 'r') as documented_rentals:
        documented_rentals.readline()
        read_rest = history.readlines()
    for lines in read_rest:
        split = lines.strip().split(', ')
        history.append([str(split[0]), str(split[1]), float(split[2]), str(split[3])])
    return history

def in_history(type_of_motorcycle, amount_of_days, total_cost):
    with open('history.txt', 'a') as history:
        history.write('\n{}, {}, ${:.2f}'.format(type_of_motorcycle, amount_of_days, total_cost))

def quantity_take_away(inventory, type_of_motorcycle, quan_of_motorcycles):
    ''' item, string, int, -> None '''
    key1, key2, key3, key4 = 'code', 'type_of_motorcycle', 'color', 'quantity'
    new_quantity = '{}, {}, {}, {}'.format(item.get(key1), item.get(key2), item.get(key3), item.get(key4))
    inventory[type_of_motorcycle]['quantity'] -= quan_of_motorcycles
    for items in inventory.values():
        new_quantity += '\n{}, {}, {}, {}'.format(items.get(key1), items.get(key2), items.get(key3), items.get(key4))
    with open('inventory.txt', 'w') as file:
        return new_quantity