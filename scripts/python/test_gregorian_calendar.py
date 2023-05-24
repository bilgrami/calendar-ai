from gregorian_calendar import generate_dates
import unittest

class TestGenerateDates(unittest.TestCase):
    def test_generate_dates(self):
        start_year = 1760
        end_year = 2650

        dates = generate_dates(start_year, end_year)

        # Assert the number of dates
        # expected_num_dates = (end_year - start_year + 1) * 365  # Assuming non-leap years by default
        expected_num_dates = 325431
        self.assertEqual(len(dates), expected_num_dates)

        # Assert the range of years
        years = set(date[1] for date in dates)
        self.assertEqual(min(years), start_year)
        self.assertEqual(max(years), end_year)

        # Assert the range of months
        months = set(date[2] for date in dates)
        self.assertEqual(min(months), 1)
        self.assertEqual(max(months), 12)

        # Assert the range of days
        days = set(date[3] for date in dates)
        self.assertEqual(min(days), 1)
        self.assertEqual(max(days), 31)

        # Assert the range of weekdays
        weekdays = set(date[4] for date in dates)
        self.assertEqual(min(weekdays), 0)
        self.assertEqual(max(weekdays), 6)


if __name__ == "__main__":
    unittest.main()
