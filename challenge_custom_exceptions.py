"""
1. Create a file name mydata2.txt and put data in it.
2. Open the file in a try block
3. Catch the FileNotFoundError exception
4. In else print the file contents
5. In finally close the file
6. Try to open the nonexistent file mydata3.txt and test to see if you caught
   the exception
"""

with open("mydata2.txt", 'w') as f:
    enter = True
    while enter:
        enter = input("Enter something to fill the file or nothing to stop: ")
        f.write(enter + '\n')

file_name = input("File name: ")        
try:
    f = open(file_name)
    
except FileNotFoundError:
    print("File not found")

else:
    print("Your file exists")
    print(f.read())

finally:
    f.close()


    

