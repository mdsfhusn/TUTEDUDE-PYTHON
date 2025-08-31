""" This for PYTHON TUTEDUDE MODULE 5 ASSIGNMENT 4 
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
 
"""
a = open('data.txt','a+')
datain = input("Enter text to write to the file : ")
a.write(datain)
print("Data successfully written to data.txt file")

datain = input("Enter additional text to append: ")
a.write(datain)
print("Data successfully appended")
print('Final Content of the data.txt file')
a.seek(0)
a.read()
a.close()

# Hence Solved
