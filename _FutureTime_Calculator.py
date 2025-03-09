def add_time(start_time, duration, start_day = None):

    # Dictionary to map days of the week to numerical values for easy calculation
    days_of_week = {
        "monday" : 0, 
        "tuesday" : 1, 
        "wednesday" : 2, 
        "thursday" : 3, 
        "friday" : 4, 
        "saturday" : 5, 
        "sunday" : 6
        }
    
    # List to retrieve days in order
    days_of_week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Extract duration hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # Extract start time details
    time_part, meridian = start_time.split()
    start_hours, start_minutes = map(int, time_part.split(":"))

    # Convert 12-hour format to 24-hour format
    if meridian == "PM" and start_hours != 12:
        start_hours += 12
    elif meridian == "AM" and start_hours == 12:
        start_hours == 0

    # Compute total minutes and hours
    total_minutes = start_minutes + duration_minutes
    extra_hours = total_minutes // 60 # Carry over extra minutes into hours
    total_minutes %= 60 # Remaining minutes
    total_hours = start_hours + duration_hours + extra_hours

    # Compute the number of days passed
    days_later = total_hours // 24
    total_hours %- 24 # Remaining hours in 24-hour format

    # Convert back to 12-hour format
    final_meridian = "AM" if total_hours < 12 else "PM"
    final_hours = 12 if total_hours % 12 == 0 else total_hours % 12

    # Format minutes properly
    final_minutes = f"{total_minutes:02d}"

    # Construct the new time string
    new_time = f"{final_hours}:{final_minutes} {final_meridian}"

    # Determine the new day if a start day was provided
    if start_day:
        start_day = start_day.lower()
        new_day_index = (days_of_week[start_day] + days_later) % 7
        new_day = days_of_week_list[new_day_index]
        new_time += f", {new_day}"

    # Append the number of days later if applicable
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time