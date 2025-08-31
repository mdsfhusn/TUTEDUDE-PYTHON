""" this file is for TUTEDUDE PYTHON MODULE 5 ASSIGNMENT 4 TASK 1
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""
try:
  file = open('sample.txt','r')
  m=0
  for a in file.readlines():
    m+=1
    print("Line ",m," : ",a)
    
except FileNotFoundError :
  print('Error : the file "sample.txt" was not found')


