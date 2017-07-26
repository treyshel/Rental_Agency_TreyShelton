def dos_inventory():
    ''' [[str, str, str]]
    >>> dos_inventory()
    [[1, '2006 Suzuki GSXR 600', 'blue and white'], [2, '2004 Yamaha R1 1000', 'red'], [3, '2001 Kawasaki Ninja ZX-9R 900', 'grey'], [4, '2016 Honda CBR 500', 'white and black'], [5, '2017 Kawasaki Ninja EX 650', 'bright green'], [6, '2009 Suzuki GSX 1000 Hayabusa', 'red and black']]
    '''
    motorcycle = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        for lines in file:
            split = lines.split(', ')
            motorcycle.append(list(split[0].strip(), str(split[1].strip()), str(split[2].strip())))
    return motorcycle