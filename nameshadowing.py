# Why to avoid naming variables/functions the names of built-in functions

# call built-in max function - works fine
print(max([1, 10, 20]))

# create variable with name max, redifining max so it no longer points to max() function
max = 5

# Now this errors because max is now an integer, not the function
print(max([1, 10, 20]))