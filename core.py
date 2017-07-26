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

