# Task 12
#
# Write some code that uses the popitem() method to remove some key:value pairs
# from the stock dictionary.

stock = {"apple": 15, "pear": 50, "watermelon": 20}
print(stock)

key, value = stock.popitem()
print(f" Removed: {key} - {value}")
print(stock)


# Output:

#  {'apple': 15, 'pear': 50, 'watermelon': 20}
#  Removed: watermelon - 20
# {'apple': 15, 'pear': 50}