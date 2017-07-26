def inventory(line, lines):
    ''' [str, [str, str]]'''
    motorcycle = {}
    key_1, key_2, key_3 = keys
    for line in lines:
        code, type_of_motorcycle, color = line.strip().split(', ')
        motorcycle[code] = {
            key_1: code, 
            key_2: type_of_motorcycle, 
            key_3: color
        }
    return motorcycle

def adding_tax(beginning_cost):
    '''float -> float
    
    adds 7% tax in to the starting cost
    
    >>> adding_tax(119.99)
    128.39
    >>> adding_tax(139.99)
    149.79
    >>> adding_tax(169.99)
    181.89
    >>> adding_tax(209.99)
    224.69
    >>> adding_tax(259.99)
    278.19
    '''
    tax_amount = beginning_cost * .07
    total_with_tax = tax_amount + beginning_cost
    return round(total_with_tax, 2)

def add_damage_deposit(cost_after_taxes):
    '''float -> float

    adds 10% to the cost after taxes to 
    cover the damage fee

    >>> add_damage_deposit(128.39)
    141.23
    >>> add_damage_deposit(149.79)
    164.77
    >>> add_damage_deposit(181.89)
    200.08
    >>> add_damage_deposit(224.69)
    247.16
    >>> add_damage_deposit(278.19)
    306.01
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

def choose_motorcycle(code):
    '''str -> str'''
    if code == '1':
        return '2006 Suzuki GSXR 600'
    elif code == '2':
        return '2004 Yamaha R1 1000'
    elif code == '3':
        return '2001 Kawasaki Ninja ZX-9R 900'
    elif code == '4':
        return '2016 Honda CBR 500'
    elif code == '5':
        return '2017 Kawasaki Ninja EX 650'
    elif code == '6':
        return '2009 Suzuki GSX 1000 Hayabusa'
