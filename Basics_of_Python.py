"""
Created on Fri Aug 21 22:12:27 2020

@author: syedheena
"""
"""
These pieces of code will help you understand the different concepts in Python. I have covered the following concepts:
    1. Simple operations
    2. Control and looping statements
    3. Data structures-Lists, tuples, and dictionaries
I have described the problem statements along with their solutions using the object-oriented programming concept only.
"""
# Problem statement 1
"""
You are given a value in Fahrenheit. You are required to convert this value into Celsius. Also, determine the following for the converted value:
    1. Print Above freezing point if temperature more than 0. Further, return Cold if the temperature is between 0 to 17, return Normal if the temperature is between 18 to 35, return Warm if temperature between 36 to 45, return Extreme heat if temperature above 45.
    2. Print Below freezing point is temperature less than 0.
    3. Print Temperature equal to freezing point if equal to 0.
"""
# Solution 1
class conv_temp:   # Creating a class 
    
    def Fah_to_Cel(self, F):    # Function that takes the value F=88 
        C = (F - 32)*5/9           # Formula 
        return C                # Returning the converted value

    def temp_determine(self, con_F_to_C_value):     # Function to determine the type of temperature
        if con_F_to_C_value == 0:
            return "Temperature equal to freezing point"
        elif con_F_to_C_value < 0:
            return "Below freezing point"
        elif 0 < con_F_to_C_value:
            print("Above freezing point")
            if 0 < con_F_to_C_value <= 17:
                return "Cold"
            elif 18 <= con_F_to_C_value <= 35:
                return "Normal"
            elif 36 <= con_F_to_C_value <= 45:
                return "Warm"
            else:
                return "Extreme heat"
        else:
            return "Invalid"   
            
obj1 = conv_temp()       # Creating an object for the class conv_temp
con_F_to_C_value = obj1.Fah_to_Cel(77)   # Storing the returned value from the function after providing F = 88
print("The converted value is {} C".format(con_F_to_C_value))   # Printing the converted value
res = obj1.temp_determine(con_F_to_C_value)  # Storing the returned value from temp_dteremine
print(res)  # Printing the result
#%%
# Problem statement 2
"""
Determing the greatest common factor of two numbers.
"""
# Solution 2
class GCD:      # Creating a class
    
    def __init__(self, a=0, b=0):       # Initializing the constructor
        self.a = a
        self.b = b
        
    def ComputeGCD(self, num1, num2):   # Creating a function that can compute the GCD of two numbers
        i = 1
        while (i <= num1 and i <= num2):
            if((num1 % i) == 0 and (num2 % i) == 0):
                g = i
            i += 1
        return g

obj2 = GCD()    # Creating an object for the class GCD
num1, num2 = map(int, input().split(","))  # Providing two inputs, for example, 87236, 88. 
# Note: The values are comma-separated.
GCD_res = obj2.ComputeGCD(num1, num2)   # Storing the computed value from ComputeGCD
print("The GCD of {}, {} is {}.".format(num1, num2, GCD_res))   # Printing the result
#%%

"""
This section will cover the concepts on lists, tuples, and dictionaries.
"""
# Problem statement 3
"""
You are given a list of numbers. You are required to perform the following tasks on this list:
    1. Add all the multiples of 2 that lie between 10 and 50.
    2. Remove any element from the list that is less than 0 and print the new list.
    3. Determine the index of elements from the list that are divisible by 5.
    4. Check if there are any elements in the list equal to 10. If yes, return the total count.
    5. Find the index of the first element in the list that is a divisible by 3 and insert 100 adjacent to it.
    6. Reverse the list and then print the sorted list.
    7. Print the length of the list.
"""
# Solution 3
class List_operations:      # Creating a class
    
    def __init__(self, l=[]):       # Initializing the constuctor
        self.l = l
        
    def add(self):      # Append operation
        for elements in range(10,51):
            if elements % 2 == 0:
                self.l.append(elements)
        return self.l
    
    def remove(self):   # Removing operation
        for i in self.l:
            if i < 0:
                self.l.remove(i)   
        return self.l
    
    def index(self):    # Index operation
        a = []
        for element in self.l:
            if element % 5 == 0:
              x = self.l.index(element)
              a.append(x)
        return tuple(a)
    
    def check(self):    # Counting operation
        count = 0
        for element in self.l:
            if element < 10:
                count += 1
        return count
    
    def insert_ele(self):       # Inserting operation
        for index in range(len(self.l)):
            if self.l[index] % 3 == 0:
                self.l.insert(index+1, 100)
            return self.l
            
    def reversing_list(self):   # Reverse and sorting operation
        self.l.reverse()
        return sorted(self.l)    
            
    def length(self):       # Using the len() function
        return len(self.l)
    
l = [33, -56, 1, 6, 10, -4, 32, -79, 100, 300]      # List of elements
obj3 = List_operations(l)       # Creating the object for the class
added_multiples = obj3.add()        # Storing the result 
print("1. Added all the multiples of 2 that lies between 10 and 50:", added_multiples)  # Printing the result 
remove_element = obj3.remove()  # Storing the result 
print("2. Removing elements that have value less than 0 and printing the new list:", remove_element) # Printing the result 
index_determination = obj3.index()      # Storing the result 
print("3. The index values that have values that are divisible by 5:", index_determination)  # Printing the result 
check_count = obj3.check()      # Storing the result 
print("4. Number of values less than 10:", check_count)  # Printing the result 
inserting_ele = obj3.insert_ele()       # Storing the result 
print("5.Inserting the element operation:", inserting_ele) # Printing the result 
rev_list = obj3.reversing_list()        # Storing the result 
print("6. The reversed and sorted list is:", rev_list) # Printing the result 
length_list = obj3.length()     # Storing the result 
print("7. The length of the final string is:", length_list) # Printing the result 

#%%
# Problem statement 4
"""
Continuing problem 3, determine the following:
    1. Average
    2. If any value is present more than one time, remove the element and print the new list
    3. Maximum value and minimum value from the new list
"""
# Solution 4

class list_extended:        # Creating the class
    
    def avg(self, l):       # Function that determines the average 
        s = 0
        for item in l:
            s += item
        return s/len(l)
    # Note: You can also use the sum() function here.
    
    def repeat(self, l):        # Function that checks if there are any elements that appear more than once
        repeat = []
        for element in l:
            if element not in repeat:
                repeat.append(element)
        return repeat
    
    def max_min(self,l):        # Function that determines the minimum and maximum element from the tuple
        return max(l), min(l)
        # Noet: This will return a tuple.

l = [1, 6, 10, 10, 12, 14, 16, 18, 18, 20, 22, 24, 24, 26, 28, 30, 32, 32, 33, 34, 36, 38, 40, 42, 44, 44, 46, 48, 50, 100, 100, 300] # Tuple
obj4 = list_extended()  # Creating an object for the class
average = obj4.avg(l)  # Storing the result 
print("1. The average of is", round(average, 2))  # Printing the result 
repeat_check = obj4.repeat(l)  # Storing the result 
print("2. The list without any repeated elements:", repeat_check)  # Printing the result 
max_min_val = obj4.max_min(l)  # Storing the result 
print("3. The maximum value is {} and the minimum value is {}:".format(max_min_val[0], max_min_val[1]))  # Printing the result 
#%%
# Problem statement 5
"""
You are given a tuple. Perform the following operations on it:
    1. Print a packed list of 2, that is, [(1,2), (3,4)]
    2. Convert it into a dictionary
    3. Add "Python" and "language" into the tuple and print the new tuple
    4. From the list obtained in 1, sort the list in ascending order based on the second element in the packed list. Print the sorted tuple.
"""
# Solution 5
class Tuple_operation:      # Creating the class
    
    def __init__(self, t = ()):     # Initializing the constructor
        self.t = t
    
    def Conv_to_list(self):     # Function that converts the tuple into a packed list
        list_t = list(zip(self.t[0::2], self.t[1::2]))
        return list_t
        
    def Conv_to_dict(self):     # Function that converts the tuple into a dictionary
        d = dict(zip(self.t[0::2], self.t[1::2]))
        return d
    
    def add_new_element(self):  # Function that addes new element in the tuple
        new = list(self.t)      # Tuple is immutable. Therefore, convert the tuple into a list.
        new.append("Python")
        new.append("language")
        return tuple(new)
    
    def sorting(self, tuple_to_list):   # Function that sorts the packed list based on the provided condition in the problem statement
        return tuple(sorted(tuple_to_list, key = lambda tuple_to_list: tuple_to_list[1]))
        
t = ("India", "Australia", "USA", "Europe", "Artic", "Antartica")       # Tuple
obj5 = Tuple_operation(t)  # Creating an object for the class
tuple_to_list = obj5.Conv_to_list()  # Storing the result 
print("1. The packed list is:", tuple_to_list)   # Printing the result 
tuple_to_dic = obj5.Conv_to_dict()   # Storing the result 
print("2. Tuple to dictionary is:", tuple_to_dic)   # Printing the result 
new_tuple = obj5.add_new_element()   # Storing the result 
print("3. The new tuple is:", new_tuple)   # Printing the result 
sorted_list = obj5.sorting(tuple_to_list)   # Storing the result 
print("4. The new tuple is:", sorted_list)  # Printing the result 
#%% 
# Problem statement 6
"""
You are given an information about the items and their prices in a store in the form of a dictionary. Perform the following operation:
    1. Print the items that have price greater then the average of all the prices.
    2. Add a new item-"Pineapple" that has a price of Rs. 100.
    3. Group items that have the same value.
    4. Print the item that has price less than Rs. 5.
"""
# Solution 6
class item_price:       # Creating the class
    
    def __init__(self, details = {}):       # Initializing the constructor
        self.details = details
    
    def avg(self):      # Function that determines the average
        avg = 0
        for items in self.details:
            avg += self.details.get(items) 
        return avg/len(self.details)
    
    def printing(self, average):        # Function that returns the items that have price greater than the average
        for items in self.details:
            if self.details.get(items) > average:
                return items
    
    def new_item(self):     # Function that adds the new item and its price
        self.details["Pineapple"] = 100
        return self.details
    
    def arrange(self):      # Function that arranges the dictionary based on the condition provided in the problem statement
        f = {} 
        for key, value in self.details.items(): 
            if value not in f: 
                f[value] = [key] 
            else: 
                f[value].append(key) 
        return f 

    def less_than_5(self):      # Function the returns the item that has its price less than 5
        y = {key:val for key, val in self.details.items() if val < 5}
        for i in y.keys():
            return i


details = {"Apple": 34, "Grapes": 45, "Banana": 15, "Onion": 34, "Tomato": 19, "Coriander": 3}  # Dictionary
obj6 = item_price(details)      # Creating the object for the class
average = obj6.avg()        # Storing the result
item_greater = obj6.printing(average)   # Storing the result
print("1. The item that has price greater than the average of all the prices:", item_greater)   # Printing the result
new_element_in_details = obj6.new_item()        # Storing the result
print("2. The new dictionary after adding the new element:", new_element_in_details)   # Printing the result
arranged_details = obj6.arrange()       # Storing the result
print("3. The new dictionary after arranging it is:", arranged_details)     # Printing the result
print_item = obj6.less_than_5()     # Storing the result
print("4. Printing the items that have price less than 5:", print_item)    # Printing the result

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    