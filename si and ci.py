# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 19:41:49 2019

@author: Dev Goel
"""

# menu() function prints the main menu, and prompts for a choice
def menu():
    #Print Option of simple and compound intrest
    print("Choose one of the following options according to your need and desire")
    print("1) Calculate simple intrest")
    print("2) Calculte compound intrest")
    print("3) Quit")
    return input("Choose your option: ")
#To get simple intrest and compound intrest
    def si(x,y,z):
        print("Simple intrest = ",x*y*z)
        def compound(a,b,c):
            print("Compound intrest = ",a * (pow((1 + b / 100), c)))
            
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        si(input("Enter the amount of principle"),input("Enter intrest rate on the princliple amount"),input("Enter the duration"))
    elif choice == 2:
        compound(input("Enter the amount of principle"),input("Enter intrest rate on the princliple amount"),input("Enter the duration"))
    elif choice == 3:
                
        
#End of program
        
        



        
        
        
        
        
        