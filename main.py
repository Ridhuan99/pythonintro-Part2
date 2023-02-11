#conditional logic
is_adult = True
has_lisence = False

if is_adult:
  print('You can drive')
else:
  print('You cannot drive')

print('----------------------')
is_adult = False

if is_adult:
  print('You can drive')
elif has_lisence:
  print('You can drive')
else:
  print('You cannot drive')

print('----------------------')
print('Correct logic')
has_lisence = True
is_adult = True

if is_adult and has_lisence:
  print('You can drive')
else:
  print('You cannot drive')

  print('identation one')
print('indentation two')

#ternary operator
#condition_is_true if condition_is_true else if_condition_is_false
print('----------------------')
is_friend = True
message = 'can message' if is_friend else 'cannot message'
print(message)
print('----------------------')
is_friend = False
message = 'can message' if is_friend else 'cannot message'
print(message)
is_user = True
if is_friend and is_user:
  print('Success')

print('----------------------')
#logical operator > < == != >= <=
print(1 > 4)
print(1 < 4)
print('a' == 'A')
print('a' != 'A')
print(1 <= 4)
print(8 >= 4)
print(not(True))

print('----------------------')
#exercise
is_magician = True
is_expert = False

#check if u magician and expert = "you are a master magician"
if is_magician and is_expert:
  print('you are master magician')
#check if magician but not expert = "at least you are getting there"
elif is_magician and not is_expert:
  print('at least you are magician')
#if you are not magician = "you need power"
else:
  print('you need magic')

print('----------------------')
# == vs is

print(True ==  1)
print('1' == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
#print('----------------------')
#print(True is 1)
#print('' is 1)
#print([] is 1)
#print(10 is 10.0)
#print([] is [])
print('----------------------')
for item in 'Hi Awak':
  print(item)
print('----------------------')
for item in [1,2,3,4]:
  print(item)
print('----------------------')
for item in [1,2,3,4]:
  for x in 'abcd':
    print(item, x)
print('----------------------')
student = {
  'name':'Ridhuan',
  'age': 24,
  'class': 'Muzannab'
}

#iterable is for collection of item list,tuple, dictionary,string
for item in student.items():
  print(item)
for item in student.values():
  print(item)
for item in student.keys():
  print(item)
for key, value in student.items():
  print(key , value)

print('----------------------')
#exercise
new_list = [1,2,3,4,5,6,7,8,9,10]
total = 0
for item in new_list:
  total = total + item

print(total)
print('----------------------')
#range
for i in range(0,10):
  print(i)
print('----------------------')
for i in range(10,0):
  print(i)
print('----------------------')
for i in range(10,0,-1):
  print(i)
print('----------------------')
for i in range(10,0,-2):
  print(i)
print('----------------------')
for _ in range(2):
  print(list(range(10)))
print('----------------------')
i = 0
while i < 5:
  print(i)
  i= i + 1
print('----------------------')
i = 0
while i < 5:
  print(i)
  break
  i = i+1
print('----------------------')
while i < 5:
  print(i)
  i = i +1
else:
  print('Finish')
print('----------------------')
my_list = [1,2,3,4,5]
i = 0
while i < len(my_list):
  print(my_list[i])
  i = i+1

while True:
  answer = input('What are you doing: ')
  if answer == 'stfu':
    break

#pass use for empty loop
print('----------------------')
i = 0
while i < len(my_list):
  i = i +1 
  continue
  print(i)
print('----------------------')
i = 0 
while i in my_list:
  pass
print('----------------------')
tree = [
  [0,0,1,0,0],
  [0,1,1,1,0],
  [1,1,1,1,1],
  [0,0,1,0,0],
  [0,0,1,0,0],
]

def print_tree():
  for i in tree:
    for x in i:
      if x == 1:
        print('*',end = '')
      else:
        print(' ', end = '')
    print('')

print('----------------------')
#exercise
listA = ['a','b','c','b','d','m','n','n']

i = 0
counter = 1
length = len(listA)
duplicate = []
while i < length:
  if listA[i] == listA[counter]:
    duplicate.append(listA[i])
    i = i+1
    counter = i+1
  else:
    counter = counter + 1
  if counter == 8:
    i = i+1
    counter = i+1
    
print(duplicate)
#function 
print_tree()
print_tree()
print_tree()
print('----------------------')
#parameterized function with default parameter
def greet(name='Anonymus', region='Malaysia'):
  print(f'Hi {name}. You live in {region}')

#argument
greet('Wanjay','Sabah')
#Positional Argument
greet(region='Sarawak',name='Loki')
greet()

print('----------------------')
#return statement
def sum(num1,num2):
  return num1 + num2
print(sum(2,4))

print('----------------------')
#Exercise
age = input("What is your age?: ")
age = int(age)
def checkDriverAge(age=0):
  if age < 18:
  	return "Sorry, you are too young to drive this car. Powering off"
  elif age > 18:
  	return "Powering On. Enjoy the ride!"
  elif age == 18:
  	return "Congratulations on your first year of driving. Enjoy the ride!"

print(checkDriverAge(age))
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

print('----------------------')
#docstring
def valA(A):
  '''
  This function is to validate and print string A
  '''
  print(A)

help(valA)
print('----------------------')
#*args and **kwargs

def check_product(*store,**items):
  print(store)
  print(items)

check_product('Mydin','Lotus','Giant',product='Darlie',price='8.00')
print('----------------------')
#Exercise
def highest_even(li):
  evennum = []
  for item in li:
    if item % 2 == 0:
      evennum.append(item)

  highest = 0
  for item in evennum:
    if item > highest:
      highest = item

  return highest

list = [10,4,6,3,2,11]
print(highest_even(list))

print('----------------------')
#walrus operator
a = 'wanjay bergerak kesana dan kesini'
if((n := len(a)) >  10):
  print(f'string a has {n} letter')

print('----------------------')
#Scope
#start with local scope
#parent local
#global
#built in function
globalparam = 1

def checkparam():
  globalparam = 2 #parent local param
  def getparam():
    return globalparam #local param
  return globalparam

print(checkparam())
print(globalparam)

print('----------------------')
#global keyword
total = 0

def increase_total():
  global total
  total += 1
  return total
increase_total()
increase_total()
print(increase_total())

print('----------------------')
#nonlocal keyword
def outer():
  x = "local"
  def inner():
    nonlocal x
    x = 'nonlocal'
    print('inner :', x)
  inner()
  print('outer :', x)

outer()

