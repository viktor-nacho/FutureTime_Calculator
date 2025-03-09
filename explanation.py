# start_time = "3:00 AM"
"""
Two reasons why it should be a string
* it contains not only numbers but alphabets too
* you can't split an integer
"""

# time_part, meridian = start_time.split()

# print(time_part)

"""
Map function() - is used to apply a given function to every item of an iterable, such as list or tuple, and dreturns a map object ( which is an iterator ).
example
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))

output
[1,2,3,4]

syntax of the map() function
map(function, iterable)

Parameter:
function : the function we want to apply to every element of the iterable
iterable : the iterable whose element we want to process

a = [1, 2, 3, 4]

# Using custom function in "function" parameter
# This function is simply doubles the provided number
def double(val):
  return val*2

res = list(map(double, a))
print(res)

map() with lambda

a = [1, 2, 3, 4]

# Using lambda function in "function" parameter
# to double each number in the list
res = list(map(lambda x: x * 2, a))
print(res)

a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))
"""


"""
This block of code converts a **12-hour format** time into a **24-hour format** time.

### **Breaking it Down:**
#### **1. Handling PM times**
```python
if meridian == 'PM':
    start_hours += 12 if start_hours != 12 else 0
```
- If the given time is **PM**, we need to convert it to 24-hour format:
  - Any hour **except 12 PM** gets **12 added** to it (e.g., 1 PM → 13, 2 PM → 14, etc.).
  - **12 PM stays as 12**, because in 24-hour format, 12 PM is already correct.
  
#### **2. Handling AM times**
```python
elif meridian == 'AM' and start_hours == 12:
    start_hours = 0
```
- If the time is **AM** and the hour is **12 (midnight)**, it should be converted to **0** (since midnight in 24-hour format is 00:00).

### **Example Conversions**
| 12-hour Format | 24-hour Format |
|---------------|--------------|
| 12:00 AM | 00:00 |
| 1:00 AM | 01:00 |
| 11:00 AM | 11:00 |
| 12:00 PM | 12:00 |
| 1:00 PM | 13:00 |
| 11:00 PM | 23:00 |

This conversion is essential when performing calculations with time, as 24-hour format simplifies addition and avoids AM/PM confusion. 🚀
"""