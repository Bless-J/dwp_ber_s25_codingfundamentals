#Variables
mynumber = 10
print(mynumber)

my_string = "Hello Python!"
print(my_string)

my_float = 3.14 
print(my_float)

#Concat
firstname = "Blessing"
lastname = "D"
fullname = firstname + " " + lastname
print(fullname)

#Arithmetic Operations
a = 5
b = 2
add_result =(a + b)
print (add_result) #addition

a = 3
b = -2
sub_result = (a - b)
print (sub_result) #subtraction

a = 500
b = 100
div_result = (a/b)
print (div_result)

a = 42
b = 400
mult_result = (a*b)
print(mult_result)

#Bool
is_greater = 5>3
print(is_greater)

is_equal = 5==3
print(is_equal)

is_smaller = 5<3
print(is_smaller)

#Boolean Operations
bool1 = True
bool2 = False

# Logical AND
and_result = bool1 and bool2
print("AND result:", and_result)  

# Logical OR
or_result = bool1 or bool2
print("OR result:", or_result)  

# Logical NOT
not_bool1 = not bool1
not_bool2 = not bool2
print("NOT bool1:", not_bool1) 
print("NOT bool2:", not_bool2) 

#Comparison between data types
pi = 3.14
pi_pi = '3.14'
pi_pi_pi = "3.14"

#1. Are `pi` and `pi_pi` equal? If not, why? Ans. they are not equal, pi is a float and pi_pi is a str. So, the comparison generate false.
#2. Are `pi_pi` and `pi_pi_pi` equal? If not, why? Ans. they are both str and have the same values.


#Type checking and conversion
print("Type of pi:", type(pi))          
print("Type of pi_pi:", type(pi_pi))    
print("Type of pi_pi_pi:", type(pi_pi_pi))

#Type conversion
my_str = "123"

# Convert the string to an integer
my_int = int(my_str)

# Convert the integer to a float
my_float_converted = float(my_int)

# Print all three variables
print("my_str:", my_str)               
print("my_int:", my_int)               
print("my_float_converted:", my_float_converted)

#Challenge
celsius = 25  
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)