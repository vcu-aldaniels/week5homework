"""Homework file for my students to have fun with some algorithms!"""

def find_greatest_number(incoming_list):
    """Required parameter, incoming_list, should be a list.
    Find the largest number in the list."""
    return max(incoming_list)
pass
  
  
def find_least_number(incoming_list):
    """Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list."""
    return min(incoming_list)
pass
     

def add_list_numbers(incoming_list):
    """Required parameter, incoming_list, should be a list.
    Add all vlaues together and return it."""
    #create a List
    incoming_list=[1,2,3,4]
    #Find the sum of the numbers in the list
    total = sum(incoming_list)
    print("The sum of this list is:", total)


def longest_value_key(incoming_dict):
    """Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function"""
    #Create list of keys
    incoming_dict = {"dog": "cat", "a": "asdfasdfasdfasdfasdf"}
    longest_value_key = max(incoming_dict, key=len)
    print(longest_value_key)
 