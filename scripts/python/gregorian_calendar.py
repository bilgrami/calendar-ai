import csv
import os

# Generate a list of dates from 1760 till 2650
start_year = 1760
end_year = 2650
dates = []

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
                date = f"{year}-{month:02d}-{day:02d}"
                weekday = (day + 2 * month + 3 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7
                dates.append([date, year, month, day, weekday])
    return dates

# Write the dates to a CSV file
def write_dates_to_file(dates):
    filename = "./data/gregorian-dates.csv"
    headers = ["date", "year", "month", "day", "weekday"]


    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)
        writer.writerows(dates)

    print(f"CSV file '{filename}' has been generated.")

dates = generate_dates(start_year, end_year)
write_dates_to_file(dates)

