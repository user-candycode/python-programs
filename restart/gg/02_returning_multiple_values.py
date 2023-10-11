# Time conversion
def return_multiple_values(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = (seconds - hours*3600 - minutes*60)
    return hours,minutes,remaining_seconds,None

hours,minutes,seconds,random = return_multiple_values(5000)

print(hours)
print(minutes)
print(seconds)
print(random)