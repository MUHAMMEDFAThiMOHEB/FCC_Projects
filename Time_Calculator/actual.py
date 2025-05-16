import math
def add_time(start, addition , day = None):
    time_items = start.split(" ")
    time_t = time_items[0].split(":")
    time_t = list(map(int, time_t))
    time_dur = time_items[1]
    dur_add = addition.split(":")
    dur_add = list(map(int, dur_add))
    days = {                     # this dictionary will be used in a feature applyed in the future
        1 : "saturday",
        2 : "sunday",
        3 : "monday",
        4 : "tuseday",
        5 : "wednesday",
        6 : "thursday",
        7 : "friday"
    }
    total_min = dur_add[1] + time_t[1]
    extra_hours = math.floor(total_min/60)
    final_min = total_min%60
    total_hours = time_t[0] + dur_add[0] + extra_hours
    final_hours = total_hours%24
    if final_hours > 12:
        final_hours = final_hours - 12
    

    if time_dur.lower() == "pm":
        limit_hr = 12 - time_t[0]
        limit_min = 60 - time_t[1]

    else:
        limit_hr = 12 + (12 - time_t[0])
        limit_min = 60 - time_t[1]

    if day != None:
        result = f"{final_hours}:{final_min:02} {time_dur} {day}"
    else:
        result = f"{final_hours}:{final_min:02} {time_dur}"
        
    if dur_add[0] < limit_hr:    #still in the same day
        if time_dur.upper() == "AM": # check if the added time will convert AM to PM
            limit_mid_hr = limit_hr -12
            limit_mid_min = 60 - time_t[1]
            if dur_add[0] > limit_mid_hr or (dur_add[0] <= limit_mid_hr and dur_add[1] > limit_mid_min): 
                time_dur = "PM"  
            else:
                time_dur = "AM"
        return result
    
    elif dur_add[0] == limit_hr:
        if dur_add[1] >= limit_min:
            time_dur = "AM"
            day = "the next day"
            return result
        
    else: #dur_add[0] > limit_hr
        remain_hr = dur_add[0] - limit_hr
        days_count = math.ceil(remain_hr/24) + 1
        fremain_hr = remain_hr % 24
        if fremain_hr >=12 and time_dur == "PM":
            time_dur = "AM"
        else:
            days_count -= 1
            if time_dur == "AM":
                time_dur = "PM"
            else:
                time_dur = "AM"
        return result

#* testing the output
def main():
    print(add_time('3:00 PM', '3:10'))                         # 6:10 PM
    print(add_time('11:30 AM', '2:32', 'Monday'))              # 2:02 PM, Monday
    print(add_time('11:43 AM', '00:20'))                       # 12:03 PM
    print(add_time('10:10 PM', '3:30'))                        # 1:40 AM (next day)
    print(add_time('11:43 PM', '24:20', 'tueSday'))            # 12:03 AM, Thursday (2 days later)
    print(add_time('6:30 PM', '205:12'))                       # 7:42 AM (9 days later)


main()