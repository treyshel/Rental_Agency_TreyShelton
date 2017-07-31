from core import *

def test_adding_tax():
    assert adding_tax(1) == 149.79
    assert adding_tax(2) == 299.58

def test_damage_deposit():
    assert damage_deposit('0660', {'0660': {'code': '0660', 'type': '2006 Suzuki GSXR 600', 'color': 'blue', 'price': 3499.99, 'quantity': 5}}) == 350.0
    assert damage_deposit('0410', {'0410': {'code': '0410', 'type': '2004 Yamaha R1 1000', 'color': 'red', 'price': 3749.99, 'quantity': 9}}) == 375.0

def test_damage_deposit_and_tax():
    assert damage_deposit_and_tax(299.60, 279.98) == 579.58

def test_valid_quantity():
    types = {'0660': {'code': '0660', 'type_of_motorcycle': '2006 Suzuki GSXR 600', 'color': 'blue', 'price': 3499.99, 'quantity': 5}, '0410': {'code': '0410', 'type_of_motorcycle': '2004 Yamaha R1 1000', 'color': 'red', 'price': 3749.99, 'quantity': 9}}
    assert valid_quantity(types, '0660', 1) == True
    assert valid_quantity(types, '0410', 10) == False

def test_choose_motorcycle():
    inventory = {
        '0660': {'code': '0660', 'type_of_motorcycle': '2006 Suzuki GSXR 600', 'color': 'blue', 'price': 3499.99, 'quantity': 5},
        '0410': {'code': '0410', 'type_of_motorcycle': '2004 Yamaha R1 1000', 'color': 'red', 'price': 3749.99, 'quantity': 9}
    }
    assert choose_motorcycle(inventory, '0660') == '2006 Suzuki GSXR 600'
    assert choose_motorcycle(inventory, '0410') == '2004 Yamaha R1 1000'