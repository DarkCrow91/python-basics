def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
print(leap_year(int(input("whats the year"))))
