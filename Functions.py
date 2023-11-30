#They are two type of functions Traditional and Pure.
###################### Pure Function ######################
#Pure function doesn't have any effect of varaibles outside its scop
list1 = [1, 2]
def add_to_list(lst, item):
    nl = lst.copy() # copy lst to nl
    nl.append(item)  # append new element in list
    return nl


print("Before calling pure function:", list1)
new_list = add_to_list(list1,3)
print("After calling pure function:", new_list)

#Benefit of pure function: Known outcome, contistent and reliable, cache, Multi-threaded programs

###################### Recursion ######################
# Recursion is a function that calles itself repeatedly until found the solution.
# recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    #Base condition
    if (disks == 1):
        print('Disk {} moves from {} to tower {}.' .format(disks, source, destination))
        return
    
    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from {} to tower {}.' .format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
hanoi(disks, 'A', 'B', 'C')

