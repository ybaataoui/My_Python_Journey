#Functions
def calculate_tax(bill, tax):
    return round((bill * tax) / 100, 2)

print('Total Tax: ', calculate_tax(175.00, 15))

print('Total Tax: ', calculate_tax(164.33, 22))