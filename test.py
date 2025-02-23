"""
clock = 29
while clock != 25:
    clock += 1
    if clock >= 60:
        clock = 0
    print(clock)
"""

hour = 11
minute = 29
while True:
    minute += 1
    if minute == 59:
        hour += 1
        if hour == 13:
            hour = 1
        minute = 0
    if minute < 10:
        print(f"{hour}:0{minute}")
    else:
        print(f"{hour}:{minute}")
    if hour == 1 and minute == 30:
        break