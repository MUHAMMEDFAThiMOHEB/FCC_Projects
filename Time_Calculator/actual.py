import math
def add_time(start: str, addition: str , day: str = None):
    time_items = start.split(" ")
    time_t = time_items[0].split(":")
    time_t = list(map(int, time_t))
    time_dur = time_items[1]
    dur_add = addition.split(":")
    dur_add = list(map(int, dur_add))
    total_min = dur_add[1] + time_t[1]
    extra_hours = math.floor(total_min/60)
    final_min = total_min%60
    total_hours = time_t[0] + dur_add[0] + extra_hours
    if total_hours % 12 == 0:
        final_hours = 12
    else:
        final_hours = total_hours % 12

#* calculate the time till the end of the current day (start argument)

    if time_dur.lower() == "am":
        if time_t[1] != 0:
            min_teod = 60 - time_t[1]
            hr_teod = 12 + (11 - time_t[0])
        else:
            min_teod = 0
            hr_teod = 12 + (12 - time_t[0])
    else:
        if time_t[1] != 0:
            min_teod = 60 - time_t[1]
            hr_teod = 11 - time_t[0]
        else:
            min_teod = 0
            hr_teod = 12 - time_t[0]

#TODO Calculate the number of days after addition operation
    if (hr_teod > dur_add[0]) or (hr_teod == dur_add[0] and min_teod >= dur_add[1]):
        #! We still in the same day after the addition operation
        #? check whether it is day or night
        #* by calculating the time required for adding time(2nd parameter) to pass in order to be at night "PM" 
        if time_dur.lower() == "am":
            if time_t[1] != 0:
                min_t2m = 60 - time_t[1]
                hr_t2m = 11 - time_t[0]
            else:
                min_teod = 0
                hr_teod = 12 - time_t[0]
            if (dur_add[0] > hr_t2m) or (dur_add[0] == hr_t2m and dur_add[1] >= min_t2m):
                time_dur = "PM"
            else:
                time_dur = "AM"
        else:
            time_dur = "PM"
        if day != None:
            result = f"{final_hours}:{final_min:02} {time_dur}, {day}"
        else:
            result = f"{final_hours}:{final_min:02} {time_dur}"


    else: # case when time added will pass the current day (day or more after)
        remains_hr = dur_add[0] - hr_teod
        remains_min = dur_add[1] - min_teod
        if remains_min < 0:
            remains_hr -= 1
            remains_min = 60 - abs(remains_min) # Now / Once we reached this step we are in 12:00 AM the next day
        days = {                     
        1 : "Saturday",
        2 : "Sunday",
        3 : "Monday",
        4 : "Tuesday",
        5 : "Wednesday",
        6 : "Thursday",
        7 : "Friday"
        }
        nofdays = math.floor((remains_hr / 24) + 1)
        holdkey = None
        for key, value in days.items():
            if day != None and value.lower() == day.lower():
                holdkey = key
                new_day_key = holdkey + nofdays
                if new_day_key > 7:
                    new_day_key = new_day_key % 7
                else:
                    new_day_key = new_day_key
                result_day = days[new_day_key]

        # tomorrow (Just the next day)
        if remains_hr < 12: 
            time_dur = "AM"
        if remains_hr > 12 and remains_hr < 24:
            time_dur = "PM"
            remains_hr -= 12
        if day != None:
            result = f"{remains_hr}:{remains_min:02} {time_dur}, {result_day} (next day)"
        else:
            result = f"{remains_hr}:{remains_min:02} {time_dur} (next day)"

        if nofdays > 1:
            if remains_hr == 24:
                remains_hr = 12
            else:
                remains_hr = remains_hr % 24
            if remains_hr > 12:
                remains_hr -= 12
                time_dur = "PM"
            elif remains_hr == 12:
                remains_hr = 12
                time_dur = "AM"
            else:
                time_dur = "AM"
            if day != None:
                result = f"{remains_hr}:{remains_min:02} {time_dur}, {result_day} ({nofdays} days later)"
            else:
                result = f"{remains_hr}:{remains_min:02} {time_dur} ({nofdays} days later)"

    return result

print(add_time('3:00 PM', '3:10'))                         # 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))              # 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))                       # 12:03 PM
print(add_time('10:10 PM', '3:30'))                        # 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))            # 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))                       # 7:42 AM (9 days later)
print(add_time('11:59 PM', '24:05'))                       # 12:04 AM (2 days later). 
print(add_time('11:59 PM', '24:05', 'Wednesday'))          # 12:04 AM, Friday (2 days later) 
print(add_time('8:16 PM', '466:02'))                       # 6:18 AM (20 days later)
print(add_time('8:16 PM', '466:02', 'tuesday'))            # 6:18 AM, Monday (20 days later)