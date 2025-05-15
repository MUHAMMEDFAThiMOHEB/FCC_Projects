"""
#! Trying to take the time as an input from the user
#? versions of time_input function (future work)
TODO --> develop an age calculator 
"""

#* version 1

import math
def time_input():
    while True:
        time = input("Enter a time in \'hh:mm:ss\' formate\nTime take in (24hr) formate --> ").replace(" ","")  
        if time.count(":") != 2:
            print("Invaild Input\nTime must be in hh:mm:ss Formate !!!")
        else:
            time_l = time.split(':')
            try:
                time_l = list(map(int(), time_l))
                return time_l
            except ValueError:
                print("String could not converted to integer !! ")


#* version 2

def time_input():
    while True:
        niody = input(f"Type ('am','pm') to choose between [Night(pm), Day(am)]")
        if niody.lower() not in ("am","pm"):
            print("Invaild Input, type am or pm ")
            continue
        else:
            time = input("Enter a time in \'hh:mm\' formate\nTime take in (12hr) formate --> ").replace(" ","")  
        if time.count(":") != 1:
            print("Invaild Input\nTime must be in hh:mm Formate !!!")
        else:
            time_l = time.split(':')
            try:
                time_l = list(map(int, time_l))
                if time_l[0] > 12:
                    print("Invalid Inpu, Hours must be < 12 !")
                if time_l[1] > 59:
                    print("Invaild Input, Minutes must be <= 59 !")
                else:
                    print(f"your input time -> {time_l[0]}:{time_l[1]}")
                    time_l.append(niody)
                    return time_l
            except ValueError:
                print("String could not converted to integer !! ")


