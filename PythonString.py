
# called Text Sequence Type - str

# Can be enclosed in single quotes, double quotes,
# triple single quotes and triple double quotes

single_quote_string = 'This is a single quoted string'
double_quote_string = "This is a double quoted string"
triple_single_quote_multiline_string = '''This is a triple single quoted
                                       multiline string
                                       And it can span many lines'''

triple_double_quote_multiline_string = """This is a triple double quoted
                                       multiline string
                                       And it can span many lines"""


# objects in object oriented programming, a class has instance variables and methods
# one can call the methods on objects
# string provides methods to manipulate strings in Python

# Following returns the position from where 'str' is found in the given string
print(single_quote_string.find('str'))

# Calling function from string constant directly without a variable assignment
print("myNameIsLakhan".find("Lak"))

print(double_quote_string.upper())

# Printing special characters like tab \t
print("PythonFor\tMachine Learning\tAI\tweb application and\tscripting")

print("I want Python to take \\ as literal rather than having special meaning")

print("How to have \"double quoted\" string inside another double quoted string")



info = "Today is Sunday"
# info[3] = "5", This will give error. Strings are immutable
first = info[0]  # Accessing the first character
print(first)

space = info[5]  # Accessing the empty space in the string
print(space)

last = info[len(info) - 1]
print(last)
# The following will produce an error since the index is out of bounds
# err = info[len(info)]

# String slicing
# The character at the end index in the string, will not be included in the substring obtained through this method.
print("String slicing")
learn_slice = "Upcoming Selenium version is going to be 4.0"
print(learn_slice[0:4]) # From the start till before the 4th index
print(learn_slice[1:7])
print(learn_slice[8:len(learn_slice)]) # From the 8th index till the end

print("String slicing with steps")
print(learn_slice[0:4]) #default step is 1
print(learn_slice[1:7:2])
print(learn_slice[0:8:5])

print("Reverse String slicing with negative steps")
print(learn_slice[4:0:-1])
print(learn_slice[7:1:-2])

print("Partial slicing with steps")
print(learn_slice[:8])  # All the characters before 'M'
print(learn_slice[8:])  # Al the characters starting from 'M'
print(learn_slice[:])  # The whole string
print(learn_slice[::-1])  # The whole string in reverse (step is -1)
