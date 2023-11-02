# def divide_by(a, b):
#     return a / b 

# try:
#     ans = divide_by(40 / 0)

# except ZeroDivisionError as e: #specific
#     print(e, "We cannot divide by zero")

# except Exception as e:
#     print("Someting went wrong!", e) # generic
    
#     print(e.__class__) #print the error class

####################### Exercice ##############################
# item = [1, 2, 3, 4, 5]

# try:
#     item = item[6]
#     print(item)
# except IndexError as e:
#     print(f"{e}, You are trying to access an index that does not exist.")
# except Exception as e:
#     print('Something went wrong', e)
#     #print(e.__class__)


try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except :
    print("Unable to locate file")

