def add_time(start, duration, day=None):

    # split the string variables to integer variables
    sta_cln = start.find(':')
    dur_cln = duration.find(':')
    hrs1 = int(start[:sta_cln])
    mins1 = int(start[sta_cln+1:sta_cln+3])
    hrs2 = int(duration[:dur_cln])
    mins2 = int(duration[dur_cln+1:dur_cln+3])
    M = start[sta_cln+4:sta_cln+7]
    if day != None:
        day = day.lower()

        # add hours and minutes seperately
    hours = hrs1 + hrs2
    mins = mins1 + mins2

    # when minutes' addition is more than 60 minutes
    if mins >= 60:
        complete_hrs = int(mins/60)
        mins = mins % 60
        hours = hours + complete_hrs

    day_count = 0

    while hours >= 12:
        hours = hours - 12

        if M == 'AM':
            M = 'PM'
        elif M == 'PM':
            M = 'AM'
            day_count += 1

    if hours == 0:
        hours = hours + 12

    dayz = day_count
    if day != None:
        while dayz > 0:
            if day == 'monday':
                day = 'tuesday'
                dayz = dayz - 1
            elif day == 'tuesday':
                day = 'wednesday'
                dayz = dayz - 1
            elif day == 'wednesday':
                day = 'thirsday'
                dayz = dayz - 1
            elif day == 'thirsday':
                day = 'friday'
                dayz = dayz - 1
            elif day == 'friday':
                day = 'saturday'
                dayz = dayz - 1
            elif day == 'saturday':
                day = 'sunday'
                dayz = dayz - 1
            elif day == 'sunday':
                day = 'monday'
                dayz = dayz - 1

    # when minutes are one digit, adds one zero in front of it
    if len(str(mins)) == 1:
        mins = "0" + str(mins)
    if day == None:
        if day_count == 0:
            new_time = f"{str(hours) + ':' + str(mins) + ' ' + M}"
        elif day_count == 1:
            new_time = f"{str(hours) + ':' + str(mins) + ' ' + M + ' (next day)'}"
        elif day_count > 1:
            new_time = f"{str(hours) + ':' + str(mins) + ' ' + M + ' (' + str(day_count) + ' days later)'}"
    else:
        day = day.capitalize()
        if day_count == 0:
            new_time = f"{str(hours) + ':' + str(mins) + ' ' + M + ', ' + day}"
        elif day_count == 1:
            new_time = f"{str(hours) + ':' + str(mins) + ' ' + M + ', ' + day + ' (next day)'}"
        elif day_count > 1:
            new_time = f"{str(hours) + ':' + str(mins) + ' ' + M + ', ' + day + ' (' + str(day_count) + ' days later)'}"
    print(new_time)
    return new_time
