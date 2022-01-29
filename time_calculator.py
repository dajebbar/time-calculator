def add_time(start, duration, one_day=None):
    new_time = 0
    day = 0
    
    hours, right = start.split(':')
    minutes, meridiem = right.split()
    duration_hours, duration_minutes = duration.split(':')
    
    minutes = int(minutes)
    if meridiem == 'PM':
        hours = int(hours) + 12
    else:
        hours = int(hours)
        
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)
    
    h = hours + duration_hours
    m = minutes + duration_minutes
    
    h = h + (m // 60)
    m = m % 60
    day = day + (h // 24)
    h = h % 24
    
    if h > 12:
        h -= 12
        meridiem = 'PM'
    elif h == 12:
      meridiem = 'PM'
    elif h == 0:
        h = 12
        meridiem = 'AM'
    else:
        meridiem = 'AM'
    
    new_time = f'{h}:{m:02d} {meridiem}'
    
    days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    if one_day:
        new_time += ", " + days_of_week[(days_of_week.index(one_day.lower()) + day) % 7].capitalize()
    
    if day > 0:
        if day == 1:
            new_time += " (next day)"
        else:
            new_time += f' ({day} days later)'

    return new_time