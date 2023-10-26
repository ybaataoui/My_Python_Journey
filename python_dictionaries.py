#dictionary do not allow duplicates, the last item will override the first one
my_d = {1: 'Test', 'name': 'Youssef' }

#my_d[2] = 'Test_2' #add new item to dict

# my_d = {1: 'Test', 'name': 'Youssef', 1: 'Not a test' } #this will print the last 1 : not a test

# del my_d[1]

for key, value in my_d.items():
    print(str(key) + ' : ' + value)