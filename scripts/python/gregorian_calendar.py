import csv
import os
from datetime import datetime, timedelta

# Generate a list of dates from 1 till 3000
start_year = 1
end_year = 3000
dates = []

def get_weekday_name_from_day_number(day_number):    
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[day_number]

def get_date_to_julian_day_number(date):
    """
    """
    jd = date.toordinal() + 1721425
    return jd

def get_date_to_julian_day_number(date):
    """
    Calculates the Julian date from a given date.
    The Julian Day Number (JD) is the number of days that have elapsed 
    since noon (12:00) on January 1, 4713 BC.

    https://en.wikipedia.org/wiki/Julian_day 

    below website can be used to verify the results
    https://planetcalc.com/503/
    For example, the Julian Day Number for March 17th, 1976 is 2442855.27332

    Looks like NASA JPL uses a different formula to calculate the Julian date
    https://ssd.jpl.nasa.gov/tools/jdc/#/cd

    Background:
    From https://planetcalc.com/503/
    Calculation of the Julian day for a given date, plus some information.

    Astronomers often need to know the difference between two dates,
    or to be able to calculate the next date of a periodic event. 
    For events that are quite far from one another, such as comet appearances, 
    the regular calendar is not well suited,
    due to the different number of days in months and leap years,
    as well as calendar reforms (Julian/Gregorian) and so on.

    Thus, Joseph Justus Scaliger, a French astronomer (1540 - 1609)
    invented Julian dates or Julian days, 
    named after his father, Julius Scaliger. 
    And, just in case the thought occurred to you,
    it is not about the Julian calendar at all

    Julian days are the counter, each day incremented by one. 
    So, if you know the value of the Julian day for one date and
    the value of the Julian day for another, 
    you can simply subtract one from another and find the difference.

    The start of Julian days, called the start of the Julian era, is defined as 
    noon of January, 1st, 4713 B.C. in the Julian calendar. 
    With this date, all known historical astronomical observations have positive Julian day numbers, 
    so all calculations are simple additions and subtractions.

    A Julian day is a fractional number, where the whole part corresponds to midday, 
    0.25 is 6:00pm, 0.5 is midnight, 0.75 is 6:00am, etc.

    Because the first two digits of a Julian day remain constant for about three centuries, 
    sometimes a shorter version of a Julian day, the Modified Julian Date is used. 
    The start of Modified Julian days (MJD) is defined as midnight of November, 17th, 1858, and

    MJD = JD - 2400000.5

    Also I should note, as a programmer, that this method - i.e. converting the calendar date to a number 
    and then using additions and subtractions - is always used by programmers. 
    
    In javascript, for example, the number of milliseconds passed 
    since January 1st, 1970, is used as such a counter.
    """
    jd = date.toordinal() + 1721425
    return jd

def get_date_to_modified_julian_day_number(jd):
    """
    From wikipedia:
        https://en.wikipedia.org/wiki/Julian_day 

    Background:
    The Julian date (JD) of any instant is the Julian day number plus the fraction of a day since the preceding noon in Universal Time. 
    Julian dates are expressed as a Julian day number with a decimal fraction added.[8] 
    For example, the Julian Date for 00:30:00.0 UT January 1, 2013, is 2 456 293.520 833.
    """    
    return jd - 2400000.5

def is_leap_year(year):
    """Determine if a year is a leap year.
    From wikipedia:
        https://en.wikipedia.org/wiki/Gregorian_calendar

        Every year that is exactly divisible by four is a leap year, except 
        for years that are exactly divisible by 100, but these centurial 
        years are leap years if they are exactly divisible by 400. For 
        example, the years 1700, 1800, and 1900 are not leap years, but 
        the year 2000 is.
            — United States Naval Observatory
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_leap_date(date):
    """Determine if a date is in a leap year."""
    return is_leap_year(date.year)

def generate_dates(start_year, end_year):
    dates = []

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            days_in_month = 31
            if month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    days_in_month = 29
                else:
                    days_in_month = 28
            elif month in [4, 6, 9, 11]:
                days_in_month = 30

            for day in range(1, days_in_month + 1):
                date_str = f"{year}-{month:02d}-{day:02d}"
                date = datetime(year, month, day)
                # weekday = (day + 2 * month + 3 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7
                weekday = date.weekday()
                julian_day_number = get_date_to_julian_day_number(date)
                modified_julian_day_number = get_date_to_modified_julian_day_number(julian_day_number)
                weekday_name = get_weekday_name_from_day_number(weekday)
                leap_date = is_leap_date(date)
                leap_year = is_leap_year(year)

                dates.append([  date_str, year, month, day, weekday, \
                                leap_date, leap_year, julian_day_number, \
                                modified_julian_day_number, weekday_name])

    return dates

# Write the dates to a CSV file
def write_dates_to_file(dates):
    filename = "./data/gregorian-dates.csv"
    headers = ["date", "year", "month", "day", "weekday", \
               "is_leap_date", "is_leap_year",\
               "julian_day_number", "modified_julian_day_number",\
               "weekday_name"]


    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)
        writer.writerows(dates)

    print(f"CSV file '{filename}' has been generated.")

if __name__ == "__main__":
    dates = generate_dates(start_year, end_year)
    write_dates_to_file(dates)
