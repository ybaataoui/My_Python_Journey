# f is for file

f = open('test.txt', mode='r')
data = f.readline()
#print(data)
f.close()

############ another way to open files #############
# with statement is used for opening and closing the file automatically and it is better in handling exceptions
with open('test.txt', 'r') as f: # we can use mode = 'r' as well
    data = f.readline()
    #print(data)

############ Create files in python #############
#The w mode will override the existing file with a new one everytime we execute the program.
#To add things to an excisting file just replace the mode w with a which stend for append

# try: # it is very important to add try and except when dealing with files
#     with open('newfile.txt', 'a') as f:
#         #f.write("This is a new file created") # write a single line
#         f.writelines(["\nThis is a new file created!", "\nThis is another line to be added."])
# except FileNotFoundError as e:
#     print("Error", e)

############ Read files #############    
# with open('test.txt', 'r') as f: # we can use mode = 'r' as well. 
#     #print(f.read(44)) # print just the first 44 of a  file
#     #print(f.readline()) # print just the first line of a file
#     data = f.readlines() # print a list of lines

#     for x in data:
#         print(x)

with open('test.txt', 'r') as f: # we can use mode = 'r' as well. when using with open it automaticlly returns a list of lines. This is the same as above statement
    #print(f.read(44)) # print just the first 44 of a  file
    #print(f.readline()) # print just the first line of a file
    #print(f.readlines()) # print a list of lines

    lines = f.readlines()
print(lines)
    