def add_time(start, duration, day = None):
    # Extracting the start time
    start_splited = start.split(" ")
    start_hour, start_min =  start_splited[0].split(":")
    meridian = start_splited[1]
        
    # Extracting the duration time
    duration_hour, duration_min =  duration.split(":")
    
    # Converting start hour to 24-hour format
    if meridian == 'PM' and start_hour != 12:
        start_hour = int(start_hour) + 12

    # Calculating total minutes
    start_total_minutes = int(start_hour) * 60 + int(start_min)
    duration_total_minutes = int(duration_hour) * 60 + int(duration_min)
    total_minutes = int(start_total_minutes) + int(duration_total_minutes)
    

    # Calculating the new time
    new_hour = int(total_minutes) // 60 % 24
    new_minute = int(total_minutes) % 60
    
    
    # Determining AM/PM
    meridian = 'AM' if new_hour < 12 else 'PM'

    
    # Converting back to 12-hour format
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12
    
    # Formatting the new time
    # if int(total_minutes) // (24 * 60) == 1
    new_time = f"{new_hour}:{str(new_minute).zfill(2)} {meridian}"
    
    
    #Checking if there is number of days passed
    days_passed = int(total_minutes) // (24 * 60)

    
    
    
    # Determining the new day
    if day is not None:
        
        new_day = day.capitalize()
        if days_passed == 1:
            new_day = (["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].index(day.capitalize()) + 1) % 7
            new_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][new_day]
        elif days_passed > 1:
            new_day = (["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].index(day.capitalize()) + days_passed) % 7
            new_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][new_day]
        new_time += f", {new_day}"
        # print("new_day:",new_day)
    #checking if the days are
    x= 0
    if days_passed == 1:
        x = " (next day)"
    elif days_passed >1:
        x = f" ({int(days_passed)} days later)"
    # print("new_time:",new_time)
    if x != 0:
        new_time = f"{new_time}{x}"
    return new_time

# Test cases
print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
