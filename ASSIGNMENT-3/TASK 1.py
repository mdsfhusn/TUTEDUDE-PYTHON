""" TUTEDUDE PYTHON ASSIGNMENT 3 TASK 1"""
""" Task 1: Calculate Factorial Using a Function """

def fac(s):
  if s>1 :
    return s*fac(s-1)
  elif s==1:
    return 1
  elif s==0:
    return 1
  elif s<0:
    return "ERROR OCCURED : FACTORIAL CANNOT BE OF A NEGATIVE ERROR, ELSE IT WILL BE IN AN INFINITE LOOP IN NEGATIVE REAL DOMAIN"

num = input("Enter a number : ")
numfac = fac(num)
print("Factorial of ",num,"is : ",numfac)

