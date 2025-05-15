import math
def add_time(start, addition , day = None):
    time_items = start.split(" ")
    time_t = time_items[0].split(":")
    time_t = list(map(int, time_t))
    time_bur = time_items[1]
    dur_add = addition.split(":")
    dur_add = list(map(int, dur_add))
    days = {
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
    return f"{final_hours:02}:{final_min:02} {time_bur}"

#* testing the output
print(add_time("11:43 PM",'24:20'))
