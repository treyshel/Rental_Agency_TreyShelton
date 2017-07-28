def motorcycle_inventory(i, inv):
    ''' [str, [str, str]]'''
    motorcycle = {}
    key_1, key_2, key_3, key_4, key_5 = i
    for key in inv:
        code, type_of_motorcycle, color, price, quantity = key.strip().split(', ')
        motorcycle[code] = {
            key_1: code, 
            key_2: type_of_motorcycle, 
            key_3: color,
            key_4: float(price),
            key_5: int(quantity)
        }
    return motorcycle

def adding_tax(tax_to_days):
    '''float -> float
    
    adds 7% tax in to the 
    days they rent it (139.99/day)
    
    >>> adding_tax(1)
    149.79
    >>> adding_tax(2)
    299.58
    '''
    tax_amount = tax_to_days * 139.99
    total = tax_amount + (tax_amount * .07)
    return round(total, 2)

def damage_deposit(deposit):
    '''float -> float

    adds 10% to cover the damage fee

    >>> add_damage_deposit(3499.99)
    350.0
    >>> add_damage_deposit(6499.99)
    650.0
    '''
    deposit_amount = deposit * .10
    return round(deposit_amount, 2)

def valid_quantity(inventory, code, motorcycle):
    ''' {{'code': str, 'type_of_motorcycle': str, 'color': str, 'quantity': int}}   
    >>> types = {'0660': {'code': '0660', 'type': '2006 Suzuki GSXR 600', 'color': 'blue', 'quantity': 5}, '0410': {'code': '0410', 'type': '2004 Yamaha R1 1000', 'color': 'red', 'quantity': 9}}
    >>> valid_quantity(types, '0660', 1)
    True
    >>> valid_quantity(types, '0410', 10)
    False
    '''
    return inventory.get(code).get('quantity', -1) >= motorcycle

def choose_motorcycle(inventory, code):
    '''str -> str'''
    if code == '0660':
        return '2006 Suzuki GSXR 600'
    elif code == '0110':
        return '2004 Yamaha R1 1000'
    elif code == '0190':
        return '2001 Kawasaki Ninja ZX-9R 900'
    elif code == '1650':
        return '2016 Honda CBR 500'
    elif code == '1765':
        return '2017 Kawasaki Ninja EX 650'
    elif code == '0910':
        return '2009 Suzuki GSX 1000 Hayabusa'



