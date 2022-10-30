def isleap(year):
    that_year = ""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                that_year = "leap"
            else:
                that_year = "not leap"
        else:
            that_year = "leap"
    else:
        that_year = "not leap"
    return that_year


print(isleap(2024))