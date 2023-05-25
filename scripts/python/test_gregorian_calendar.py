from datetime import datetime, timedelta, date
from gregorian_calendar import \
    generate_dates, get_date_to_julian_day_number, is_leap_date, is_leap_year
import unittest

class TestGenerateDates(unittest.TestCase):
    """
    A class used to test the functions related to generating gregorian calendar dates
    """

    start_year = 1760
    end_year = 2650
    dates = None

    @classmethod
    def setUpClass(cls):
        """
        This method will be called once for this test case class.
        It generates the dates between start year and end year.
        """
        cls.start_year = 1760
        cls.end_year = 2650
        cls.dates = generate_dates(cls.start_year, cls.end_year)

    def setUp(self):
        """
        This method will be called before each test.
        It checks if the dates were successfully generated.
        """
        self.assertIsNotNone(self.dates)

    def test_generate_dates(self):
        """
        This test checks if the number of generated dates is as expected and
        whether the years, months, and days fall in the expected ranges.
        """
 
        # Assert the number of dates
        expected_num_dates = 325431
        self.assertEqual(len(self.dates), expected_num_dates)

        # Assert the range of years
        years = set(date[1] for date in self.dates)
        self.assertEqual(min(years), self.start_year)
        self.assertEqual(max(years), self.end_year)

        # Assert the range of months
        months = set(date[2] for date in self.dates)
        self.assertEqual(min(months), 1)
        self.assertEqual(max(months), 12)

        # Assert the range of days
        days = set(date[3] for date in self.dates)
        self.assertEqual(min(days), 1)
        self.assertEqual(max(days), 31)

    def test_get_date_to_julian_day_number(self):
        """
        This test checks the conversion of certain dates to Julian Day Numbers.
        """

        # Test a known date and expected Julian date
        self.assertEqual(get_date_to_julian_day_number(date(1998, 5, 28)), 2450962)

        # Test the start and end dates
        self.assertEqual(get_date_to_julian_day_number(date(1, 1, 1)), 1721426)
        self.assertEqual(get_date_to_julian_day_number(date(3000, 1, 1)), 2816788)

        # Test some random dates
        self.assertEqual(get_date_to_julian_day_number(date(1000, 1, 1)), 2086303)
        self.assertEqual(get_date_to_julian_day_number(date(1999, 12, 31)), 2451544)
        self.assertEqual(get_date_to_julian_day_number(date(2021, 9, 30)), 2459488)

    def test_is_leap_year(self):
        """
        This test checks the function that determines whether a year is a leap year.
        """
        assert is_leap_year(2000) == True, "2000 is a leap year"
        assert is_leap_year(2001) == False, "2001 is not a leap year"

    def test_is_leap_date(self):
        date_in_leap_year = datetime.strptime("29-02-2000", "%d-%m-%Y")
        date_not_in_leap_year = datetime.strptime("28-02-2001", "%d-%m-%Y")
        assert is_leap_date(date_in_leap_year) == True, "February 29, 2000 is in a leap year"
        assert is_leap_date(date_not_in_leap_year) == False, "February 28, 2001 is not in a leap year"

    def test_get_weekday(self):
        """
        This test checks the function that determines whether a date is in a leap year.
        """
        # Assert the range of weekdays
        weekdays = set(date[4] for date in self.dates)
        self.assertEqual(min(weekdays), 0)
        self.assertEqual(max(weekdays), 6)

if __name__ == "__main__":
    unittest.main()
