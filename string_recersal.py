#Slice Function to reverse a string
# str[start:stop:step]

trail = "reversal"
new_trail = trail[::-1] #The negative value of the step parameter indicates that the string needs to be traversed from the right one index position at a time.
print(new_trail)

################### Recursion ##################
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
str = "Youssef"
reverse = string_reverse(str)
print(reverse)