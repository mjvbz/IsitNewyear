## A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime

# Import the datetime module and display the current date:
now = datetime.datetime.now()
print(now)

"""
When we execute the code from the example above the result will be:
2021-11-21 17:55:42.929243
The date contains year, month, day, hour, minute, second, and microsecond.
The datetime module has many methods to return information about the date object.
Here are a few examples, you will learn more about them 
"""

# 2nd example
# Return the year and name of weekday:

datetime = datetime.datetime.now()

print(xdatetime.year)
print(datetime.strftime("%A"))

# 3rd example
"""
To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.
"""
# Create a date object:

x = datetime.datetime(2020, 5, 17)
print(x)

""" 
The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional,
and has a default value of 0, (None for timezone).
"""

# 4th example
"""
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
"""

# Display the name of the month:
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# check more about this at https://www.w3schools.com/python/python_datetime.asp
