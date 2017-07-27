def inventory(read_line, read_lines):
    ''' [str, [str, str]]'''
    motorcycle = {}
    key_1, key_2, key_3, key_4 = keys
    for keys in lines:
        code, type_of_motorcycle, color, quantity = keys.strip().split(', ')
        motorcycle[code] = {
            key_1: code, 
            key_2: type_of_motorcycle, 
            key_3: color,
            key_4: quantity
        }
    return motorcycle

def adding_tax(beginning_cost):
    '''float -> float
    
    adds 7% tax in to the starting cost
    
    >>> adding_tax(139.99)
    149.79
    >>> adding_tax(279.98)
    299.58
    '''
    tax_amount = beginning_cost * .07
    total_with_tax = tax_amount + beginning_cost
    return round(total_with_tax, 2)

def add_damage_deposit(cost_after_taxes):
    '''float -> float

    adds 10% to the cost after taxes to 
    cover the damage fee

    >>> add_damage_deposit(149.79)
    164.77
    >>> add_damage_deposit(290.58)
    319.64
    '''
    deposit_amount = cost_after_taxes * .10
    total = deposit_amount + cost_after_taxes
    return round(total, 2)

def return_deposit(deposit):
    '''float -> float

    returns the deposit back to customer
    if no damage is done to rental bike
    (deposit: 10% of total price)
    >>> return_deposit(141.23)
    12.84
    >>> return_deposit(164.77)
    14.98
    '''
    deposit = add_damage_deposit(cost_after_taxes) - adding_tax(beginning_cost)
    return round(deposit, 2)

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



