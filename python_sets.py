#sets differe sligtly from list in which they do not allow duplicates.
#sets are not sequences which means you can't access items based on index and they are not ordered
set_a = {1, 2, 3, 4, 5, 5}

# set_a.add(6) #insert 6 to the set
# set_a.remove(2) #delete item 2
# set_a.discard(3) #delete item 3

set_b = {4, 5, 6, 7, 8}

print(set_a.union(set_b)) # join the two sets, but without duplicate.
print(set_a | set_b) # Same thing as a bove

print(set_a.intersection(set_b)) # get the items that are in both a and b
print(set_a & set_b) # Same thing as a bove

print(set_a.difference(set_b)) # get the items that are in a and not b
print(set_a - set_b) # Same thing as a bove

print(set_a.symmetric_difference(set_b)) # get the items that are in a and b, but not both of them
print(set_a ^ set_b) # Same thing as a bove