def cuckoo_clock(initial_time, n):
    hours, minutes = initial_time.split(':')
    hours, minutes = int(hours), int(minutes)

    if (minutes % 15 == 0 and minutes > 0):
        n -=1

    while 0 < minutes < 60 and n > 0:
        minutes = int(minutes / 15)  * 15 + 15
        if minutes == 60: minutes = 0; hours += 1; break
        n -= 1
    
    while n > 0:
        if hours > 12: hours -= 12
        
        if n >= hours: n -= hours
        elif n < hours: break

        if n > 3: n -= 3; hours += 1
        else: minutes = n * 15; break

    return "{:02d}".format(hours) + ':' + "{:02d}".format(minutes)


print(cuckoo_clock("09:53", 50))