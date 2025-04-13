def add_time(start_time, duration, day=''):
    
    
    start_hour, start_minute = start_time.split(':')
    duration_hour, duration_minute = duration.split(':')
    start_minute, time_saving = start_minute.split(" ")
   
    hours = int(start_hour) + int(duration_hour)
    minutes = int(start_minute) + int(duration_minute)
    
    extra_hour, extra_minute= calculate_additional_hours(minutes) 
    
    hours += extra_hour
    minutes = f'{extra_minute:02d}' 
  
    hours, time_saving, days = reduce_hours(hours,time_saving)

    
    new_time = format_time(hours, minutes,time_saving) 

    if day:
        day = get_day(day,days)
        new_time += f', {day}'

    if days == 1:
        new_time += ' (next day)'
    elif days >1:
        new_time += f' ({days} days later)'

    return new_time


def calculate_additional_hours(minutes):
    if minutes > 60:
        hours = minutes // 60
        remainder = minutes % 60
        return hours, remainder
    else:
        return 0, minutes


def reduce_hours(t_hours, time_saving, days =0): 
    
    if t_hours >= 12:
        if time_saving == 'PM':
            time_saving = 'AM'
            days += 1
        else: 
            time_saving = 'PM'
    
    if not t_hours > 12:
        return t_hours, time_saving, days

    return reduce_hours(t_hours-12, time_saving, days)

def format_time(hours, minutes, time_saving):
        return  f'{hours}:{minutes} {time_saving}'

def get_day(_day, days_passed):
    Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday']
    day = Days.index(_day.capitalize()) if _day else None

    
    day += days_passed
    if day > (len(Days)):
        day = Days[day % (len(Days))]
    else:
        day = Days[day]
    return day
    

add_time('8:16 PM', '466:02', 'tuesday')
