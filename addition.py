def add(a, b):
    return a + b

def sub(a, b):
    return a - b

sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)

def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()