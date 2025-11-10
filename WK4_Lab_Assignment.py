#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


# Week 4 Lab: Lists, Strings, and Tuples
import datetime
print("Run time:", datetime.datetime.now())

# Define a string, list, and tuple
my_string = "Hello, GitHub!"          # A basic string
my_list = [10, 20, 30, 40, 50]        # A simple list of integers
my_tuple = (100, 200, 300)            # A tuple (immutable list)

# Display the values
print("String:", my_string)
print("List:", my_list)
print("Tuple:", my_tuple)

# Lab Assignment List
# Create a list with the given values
numbers = [22, 45, 78, 98, 100]

# Initialize a counter to zero
count = 0

# Use a loop to manually count items (without len() or count())
for item in numbers:
    count += 1                        # Increment the counter for each element

# Step 3: Display the result
print("The list contains", count, "items.")


# In[ ]:




