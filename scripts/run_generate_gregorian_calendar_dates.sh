rm -f ./data/gregorian-dates.csv
python ./python/gregorian_calendar.py
cp -f ./data/gregorian-dates.csv ../data/gregorian-dates.csv
