# List accessing
n = [1,2,3]
print(n[1])

# List element modification
n = [1, 3, 5]
# Do your multiplication here
n[1] = n[1] * 5
print(n)

# Appending to a list
n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print(n)

# Removing elements from lists
n = [1, 3, 5]
# Remove the first item in the list here
n.remove(1)
print(n)

# Changing the functionality of a function
number = 5

def my_function(x):
    return x * 3

print(my_function(number))

# More than one argument
m = 5
n = 13
# Add add_function here!
def add_function(x, y):
 return x + y

print(add_function(m, n))

# Strings in functions
n = "Hello"
# Your function here!
def string_function (s):
 return s +'world'
print(string_function(n))

# Using an element from a list in a function
def list_function(x):
    return x[1]

n = [3, 5, 7]
print(list_function(n))

# Modifying an element of a list in a function
def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print(list_function(n))

# List manipulation in functions
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
  lst.append(9)
  return lst
print(list_extender(n))

# Printing out a list item by item in a function
n = [3, 5, 7]


def print_list(x):
    for i in range(0, len(x)):
        print(
        x[i])


print_list(n)

# Modifying each element in a list in a function
n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
# Don't forget to return your new list!

print(double_list(n))

# Passing a range into a function
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print(my_function(range(3))) # Add your range between the parentheses!

# Iterating over a list in a function
n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(0,len(numbers)):
    result += numbers[i]
  return result

# Using strings in lists in functions
n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print(join_strings(n))

# Using two lists as two arguments in a function
m = [1, 2, 3]
n = [4, 5, 6]


# Add your code here!
def join_lists(x, y):
    return x + y


print(
join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]

# Using a list of lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print(flatten(n))