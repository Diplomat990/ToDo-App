''''
prompt = 'Enter a todo: '
todo1 = input(prompt)
todo2 = input(prompt)
todo3 = input(prompt)
todos = [todo1, todo2, todo3]
print(type(todos))


#bonus check input length
text = input('Enter a title: ')
length = len(text)
print('The lenghth of the book title is :' ,length)


#Creating a todo list
prompt = 'Enter a Todo: '
#storing the todos in a list
todos = []

while True:
    todo = input(prompt)
    todos.append(todo) #this would store the inputs in the empty todos[]
    print(todos.title())


#check if password is correct using an operator
password = input('Enter password: ') #user password wld be stored in this variable

while password != 'pass123':
    print('Password incorrect')
    password = input('Enter password: ')

print('Password correct')


#produce a series of numbers with while loop using comparison operator
x = 0

while x <= 5:
    x = x + 1
    print(x)

x = 1
while x > 2:
    print('yes')

#capitalize first letter and print name infinitely
user = input('what is your name: ')
print(user.capitalize())
while True:
    print(user.title())
'''


'''
#Create a program that does the following:
#Prompts the user to input the country they are from.
#If the user enters the word USA, the program prints out Hello.
#If the user enters the word  India, the program prints out Namaste.
#If the user enters the word Germany, the program prints out Hallo.
user = input('Enter your home country: ')
match user:
    case 'USA':
        print('Hello')
    case 'India':
        print('Namaste')
    case 'Germany':
        print('Hallo')
#ngredients = ["john smith", "sen plakay", "dora ngacely"]
#Copy-paste the above line into your IDE and write a for-loop below that line that makes the program produce the following output:

ingredients = ["john smith", "sen plakay", "dora ngacely"]
for i in ingredients:
    print(i.title())

#data mutability, change the . in each file name to a -, list are mutable and strings immutable, strings can be altered by .replace with a new  var
filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentation.txt']
for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)


#calculate $ to €
amount = int(input('How much exchange: '))
total = 0.95 * amount
print(total)


#create a program that returns the name of the individual on the list
ranking = [ 'John', 'Sen', 'Lisa']
rank = int(input('Check ranks: '))
position = ranking[rank]
print(position)

#create a program that returns the rank of the individual on the list, using .index to return the first value
ranking = [ 'John', 'Sen', 'Lisa']
name = input('Input user name to find position: ')
rank = ranking.index(name) + 1
print(rank)

#replace b with x in the list
elements = ['a', 'b', 'c']
new = 'x'
elements[1] = new
print(elements)

#program to sort out list alphabetically with sort and place a number before each of the output using a for loop

waiting_list = ['Sen', 'Ben', 'Tim']

waiting_list.sort

for index, item in enumerate(waiting_list):
    row = f'{index + 1}.{item.capitalize()}'
    print(row)

#put the list in a manner in wc the user can chose wc item on the list to see.
ips = ['100.122.133.105', '100.122.133.111']
index = int(input('Type in 0 or 1: '))
position = ips[index]
print(position)


#write a program to generate 3 .txt files in d dir, each file wld contain its corresponding content.

contents = ['All carrots are to be sliced longitudinally',
            'How were the carrots slice',
            'No mercy for carrots']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#creates the .txt files first along with content as txt created
for content, filename in zip(contents, filenames):
    file = open(f'file/{filename}', 'w')
    file.write(content)


#read files in a txt
file = open('file/essay.txt', 'r') #to show wat is in todos.txt
files = file.read()
print(len(files))



#Please download the members.txt file from the resources of this article.
#Then, create a program that, whenever executed, asks the user to enter a new member in the command line:
#Then, the member is added to members.txt. In this case, the text file content would be:
#John Smith
#Sen Lakmi
#Sono Octonot
#Solomon Right


new_member = input('Enter your F and L Name: ')

file = open('file/members.txt', 'r')
existing_member = file.readlines()
file.close()

existing_member.append(new_member + '\n')

file = open('member.txt', 'w')
existing_member = file.writelines(existing_member)
file.close()

#write in the list txt.
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for file in filenames:
    files = open(file, 'w')
    files.write('Hello\n')
    files.write('Hello\n')
    files.close()



#list comprehension to change the filenames contents and include .txt

filenames = ['1.doc', '1.report', '1.presentation']

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]
print(filenames)


###
names = ["john smith", "jay santi", "eva kuki"]
new_names = [name.title() for name in names]
print(new_names)

usernames = ["john 1990", "alberta1970", "magnola2000"]
new = [len(chars)for chars in usernames]
print(new)

user_entries = ['10', '19.1', '20']
float = [float(item) for item in user_entries]
print(sum(float))



#journal app
date = input("Enter today's date: ")
mood = input('What is your mood like today: ')
thoughts = input('What is on your mind:\n ') #\n to create a breakline

with open(f'./journal/{date}.txt', 'w') as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)


#A client wants to buy a coin-flip probability program from you.
# #The programs should work like this:1. The user runs the program. The program asks the user to enter "head" or "tail".  The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail". The user does the same over and over again.
while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")



#check strength of password program
password = input('Enter new password: ')
result = {} #to add to a dict we use
#checks if the password is more or less than 8 digits
if len(password) >=8:
    result['length'] = True
else:
    result['length'] = False

#isdigit is used to check if there is a number in a str.
#below code is used to check if there is a number attached in the pswrd
digit = False
for i in password:
    if i.isdigit():
        digit = True
result['digits'] = digit

#check if there is uppercase in the pswrd
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result['upper-case'] = uppercase

#all func returns true wen all results are true
print(all(result))
if all(result):
    print('Strong Password')
else:
    print('Weak Password')
print(result)

#Write a program that asks users to enter a password. Then, it checks if the password length is greater than 7 and returns "Great password there!".
#Extend the program we built in Coding Exercise 1 by adding a new feature. The new feature should allow the program to return "Password is OK, but not too strong" when the password is exactly seven characters long.
password = input('Type a password: ')
result = {}
if len(password) >= 7:
    result['length'] = True
    print('Great password there')
elif len(password) == 7:
    print('Password is ok, not too strong')
else:
    print('Password is weak')


#calculate area
try:
    width = float(input('Enter rectangle width: '))
    length = float(('Enter rectangle length: '))
    if width == length:
        exit('Looks like a square')
    area = width * length
    print(area)
except ValueError:
    print('Please enter a number.')

#generates a random whole number between 2 inputed values

#Your task is to create a program that generates a random whole number. Here is how the program should behave:
#the program first asks the user to enter a whole number. Then, once the user enters a number, the program asks the user again to enter another number.
#Then, the program returns a random number that falls between the two whole numbers. Here is another example:

import random

lower = int(input('Enter a lower number: '))
upper = int(input('Enter a upper number: '))


rand = random.randint (lower,upper )
print(rand)




#percentage calculator
try:
    total_value = int(input('Enter total value: '))
    value = int(input('Enter value: '))
    percentage = value / total_value * 100
    print(f'That is {percentage}%')
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero to divide.")


#The code below is incomplete. It should calculate and print out the maximum value of the grades list. Please complete the function and then call it.
#Hint: You can use the max(list) function to find the maximal value of a list.
#The function we wrote in exercise 1 returned 9.7.  Change the function so this time it returns Max: 9.7, Min: 9.2 where 9.7 is the maximum and 9.2 is the minimum.

def get_max():
    grades = [9.6, 9.2, 9.7]
    max_number = max(grades)
    min_number = min(grades)
    print('The largest number is', max_number, 'The minimum number is', min_number )
get_max()






#Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.
def liters_to_m3(liters):
    m3 = liters / 1000
    return m3

#Create a script that asks the user to enter a password. Then create a function that checks the strength of the user password. The function should return Strong Password if all of the following conditions are true:

user_password = input('Enter new password: ')
 #to add to a dict we use
#checks if the password is more or less than 8 digits
def strength(password):
    result = {}
    
    if len(password) >= 8:
        result['length'] = True
    else:
        result['length'] = False

    #isdigit is used to check if there is a number in a str.
    #below code is used to check if there is a number attached in the pswrd
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result['digits'] = digit

    #check if there is uppercase in the pswrd
    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result['upper-case'] = uppercase

    #all func returns true wen all results are true
    print(all(result))
    if all(result):
        print('Strong Password')
    else:
        print('Weak Password')
print(strength(user_password))


#Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature. In other words, the function has a temperature parameter and returns either "Gas", "Liquid" or "Solid" as a string depending on the temperature.
# Therefore, your task is to modify the script from exercise 1 by creating two global variables/constants in that file, one variable associated with 0 and another associated with 100. Then, use those variables in the function instead of the values.

#1
def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    else:
        return "Gas"
#2
import functions #this should be in a diff file so its imported
temperature = float(input('Enter water temperature: '))
state = functions.water_state(temperature)
print(state)

#convert feet to meters feet*0.3048 + inches * 0.0254 and see if a child is legal height to use rollercoaster


feet_inches = input('Enter feet and inches: ')
def parse(feet_inches):
    parts = feet_inches.split(' ')  # .split() the input from the user eg 5 7 = ['5', '7']
    feet = float(parts[0])  # get first item after split
    inches = float(parts[1])  # get 2nd item after split
    return {'feet': feet, 'inches':inches}

def convert(feet,inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print('Child too small to use slide')
else:
    print('Kid can use the slide')



#Define a function that has two parameters, year_of_birth and current_year . The current_year parameter should be a default parameter with the current year as a default value.
#The function should calculate and return the age of the user given the year of birth and the current year.
#Then, below the function definition, get the year of birth from the user using an input function and then call and print the defined function to get the user's age as output.
#Extend the program you wrote in exercise 2 by printing a message to the user instead of their age if their age is greater than 120. Feel free to print any message


year = int(input('Enter year of birth: '))

def age(year_of_birth, current_year=2023):
    current_age = current_year - year_of_birth
    return current_age

current_age = age(year)
if current_age > 120:
    print(f" You are {current_age} years old, Celebrate life")
else:
    print(f" You are {current_age} years old ")
    
    
#web search with google

import webbrowser

user_term = input('Enter a search term: ')

webbrowser.open("https://www.google.com/search?q=" + user_term)    
    
    
    
#Write a program that gets a list of names from the user and returns the number of names given. You are encouraged to use a function.

names = input('what are your names by commas: ')
def get_num_items(user_input):
    items = user_input.split(',')
    return len(items)
num_items = get_num_items(names)
print(num_items)

#find average temp

def get_average():
    with open('files/data.txt', 'r') as files:
        data = files.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local

average = get_average()
print(average)


#building a quiz game with json
import json
#data of questions are in a seperate json file

with open('questions.json', 'r') as file:
    content = file.read()

data = json.loads(content) #print it out as a list



for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(index + 1, '-', alternative)
    user_choice = int(input('Enter your answer: '))
    question['user_choice'] = user_choice

score = 0

for index, question in enumerate(data):
    if question['user_choice'] == question ['correct_answer']:
        score = score + 1
        result = 'correct answer'
    else:
        result = 'wrong answer'


    message = f"{result} {index + 1} - Your answer is: {question['user_choice']}, "\
            f"correct answer: {question['user_choice']}"
    print(message)


print(data)
print(score, '/', len(data))
'''



#Todo App

 #allow the user add or see inputed todo using matchcase statement

import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('it is ', now)
while True:
    user_action = input('Type Add, Show ,Edit, Complete or Exit: ')
    user_action = user_action.strip() #keeps the input valid even wen user inputs has a space mistake

    #match user_action: #to match/case the var the user typed add or show
    if user_action.startswith('Add'):
        todo = user_action[4:] #list slicing

        #file = open('todo.txt', 'r')
        #¢todos = file.readlines()
        #file.close()

        #read files content easier method using with and as, no need to close file like above code and less code
        todos = functions.get_todos()


        todos.append(todo + '\n')

#store the list item in the created todo.txt file,1st create a file var
        #file = open('todo.txt', 'w')
        #file.writelines(todos)#this wld make the todo items written to be saved in the todo.txt
        #file.close()

        #replacing the above code with shorter code to write files
        functions.write_todos(todos, 'todo.txt')


    elif user_action.startswith('Show'):

        #file = open('todos.txt', 'r') #to show wat is in todos.txt
        #todos = file.readlines()
        #file.close()

        # replacing the above code with shorter code to read files
        todos = functions.get_todos()


#list comprehension , wen u want to modify items on a list, always begins with [], #to remove the /n when the list is printed out.
        #new_todos = [item.strip('\n') for item in todos]



        for index, item in enumerate(todos): #add numbers to printed out list
            row = f"{index + 1}.{item}"
            print(row)

#to edit the todo list using list indexing system
    elif user_action.startswith('Edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1 #incase the user enter normal numbers 1,2,3 so it can match with python indexing beginnning with 0

            todos = functions.get_todos()

            new_todo = input('Enter new Todo: ')
            todos[number] = new_todo + '\n'  #this replaces the edited todo item

            functions.write_todos('todo.txt', todos)

        except ValueError:
            print('Your command is not valid.')
            continue #to run the input commands again

    elif user_action.startswith('Complete'): #use complete to manipulate the list, ie remove one item using remove
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos('todo.txt', todos)

            message = f'Todo{todo_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print('No item with that number')
            continue

    elif user_action.startswith('Exit'):
        break
    else:
        print('Command is not valid')

print('Todo list Exited')































