#Getting familiar, practice, and notes exponent functions! :) 

#Note: Allows us to take a certain number and raise it to a power

#how to use a forloop to make an exponent function
def raise_to_power(base_num , pow_num):
    result = 1
    for index in range (pow_num): #A range will range us through a collection of numbers
        result = result * base_num    #The actual result of the math is stored in the result variable; basically cubing it; 
        #the math will keep getting stored in result and so redult will become the same number as base_num
    return result

print(raise_to_power(3, 4)) #the numbers are the base_num and power_num

