# 1
def hello():
    print("goabest!")
   
# 2
def sum(a, b):
    print(a + b)

# caling function
sum(3, 5) # will print 8

# 3
def to_string(value):
    print(str(value))

# caling funktion
to_string(45) # will print '45'4
to_string(3.5) # will print '3.5'
to_string(True) # will print 'True'

# 4
def print_type(value):

    # caling funktion
    print_type(45) # will print <class 'int'>
    print_type(3.14) # will print <class 'float'>
    print_type("hello") # will print <class 'str'>
    print_type(1, 2, 3) # will print <class 'list'>


# 5
def to_integer(value):
    print(int(value))

# caling funktion
to_integer(3.14)
to_integer("45")
to_integer(True)
to_integer()