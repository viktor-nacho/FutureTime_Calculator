# FutureTime_Calculator
## Overview
The **FutureTime Calculator** is a Python function that takes a starting time, a duration, and an optional starting day to calculate the new time after adding the duration. It also determines whether the new time falls on the next day or multiple days later.

## Features
- Converts between 12-hour and 24-hour formats for accurate calculations.
- Accounts for AM/PM transitions when adding hours.
- Computes the number of days that have passed after adding the duration.
- Optionally determines the new day of the week.
- Formats the output to include information about whether the time falls on the next day or several days later.

## Usage
```python
from time_calculator import add_time

# Example 1: Basic time addition
print(add_time("3:00 PM", "3:10"))  # Output: "6:10 PM"

# Example 2: Crossing AM/PM boundary
print(add_time("11:30 AM", "2:32"))  # Output: "2:02 PM"

# Example 3: Crossing over to the next day
print(add_time("11:43 PM", "24:20"))  # Output: "12:03 AM (next day)"

# Example 4: Including a starting day
print(add_time("10:10 PM", "3:30", "Wednesday"))  # Output: "1:40 AM, Thursday"
```

## Installation
No external libraries are required. Just include the `time_calculator.py` file in your Python project and import the function.

## License
This project is open-source and available for modification and distribution under the MIT License.
