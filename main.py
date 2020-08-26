"""Write a function called list_unpacker. This function takes one parameter, a list of length 3, as an argument. The function should return the 3 values from the list, in the order the are found in the list.

Note:

    There are multiple ways to do this, but be sure to use list unpacking within the function
    It is possible to return more than one value out of a function, this is a new concept. To do so, simply separate the individual items you're returning with a comma. See below for a brief example:

# This function returns the integers 1, 2, and 3
def my_function():
    return 1, 2, 3

    """


list_len3 = ['A','B','C']
def list_unpacker(list_len3):
  A, B, C, D = list_len3
  return (A, B, C, D)

# print(list_unpacker(list_len3))


# def my_function():
#   return 1, 2, 3

# print(my_function())