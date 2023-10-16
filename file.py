num1 = 42 #variable declaration, data type number
num2 = 2.3 #variable declaration, data type float
boolean = True #variable declaration, data type boolean
string = 'Hello World' #variable declaration, data type string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, data type list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, data type diccionary
fruit = ('blueberry', 'strawberry', 'banana') #varible declaration, data type tuples
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, variable check index 1 
pizza_toppings.append('Mushrooms')# list add value
print(person['name'])#log statement, diccionary access value 'name'
person['name'] = 'George'#initialize diccionary, change value index name = george 
person['eye_color'] = 'blue' #initialize diccionary, add value 'eye_color' 
print(fruit[2]) #log statement, variable check index 2

if num1 > 45:               #conditional if 
    print("It's greater")   #log statement
else:                       #conditional else
    print("It's lower")

if len(string) < 5:         #conditional if,length check  
    print("It's a short word!")
elif len(string) > 15:      #conditional else if 
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop() #list delete value, last value
pizza_toppings.pop(1) #list delete value, value index 1

print(person) #log statement, diccionary 
person.pop('eye_color') #list delete value
print(person) #log statement, diccionary

for topping in pizza_toppings:      #for loop
    if topping == 'Pepperoni': #conditional if
        continue #for loop continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #for loop break

def print_hello_ten_times(): #function 
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):#function
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):#function
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #call function
print_hello_x_or_ten_times(4) #call function, value 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)