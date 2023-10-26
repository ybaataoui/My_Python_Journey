#Loops        
favorites = ["Creme Brulee", "Apple Pie", "Churros", "Homoss", "Chocolate Cake"]

for idx, item in enumerate(favorites):
    print(idx, item)


count = 0

while count < len(favorites):
    print('I like this desert', favorites[count])
    count += 1

#outer loop
for i in range(10):
    #inner loop
    for j in range(10):
        print(0, end = ' ')
    print()
