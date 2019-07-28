#Request a name of the file
#Read the inputted file
#display the content line by line with while loop
#save the line into list by using append function

flie_name = input("Plese input fileName: ")
handle = open(flie_name,'r')
print(type(handle))
# content = handle.read()
my_list = []
linebyline = handle.readline()
while linebyline:
    print(linebyline.strip())    
    linebyline = handle.readline()
    my_list.append(linebyline)   

print("List[]: ",my_list)
    


