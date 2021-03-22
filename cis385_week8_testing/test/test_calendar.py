import unittest
from datetime import datetime
from unittest.mock import MagicMock

from app.main import calendar
from app.main.holiday import Holiday


class TestCalendar(unittest.TestCase):

    def setUp(self):
        holiday = Holiday()
        holiday.is_new_year_observed = MagicMock(return_value=False)

    def tearDown(self):
        pass

    def test_is_leap_year_returns_true_for_leap_years(self):
        self.assertTrue(calendar.is_leap_year(1984))
        self.assertTrue(calendar.is_leap_year(2000))
        self.assertTrue(calendar.is_leap_year(2016))
        self.assertTrue(calendar.is_leap_year(2020))

    def test_is_leap_year_returns_false_for_nonleap_years(self):
        self.assertFalse(calendar.is_leap_year(1900))
        self.assertFalse(calendar.is_leap_year(2015))
        self.assertFalse(calendar.is_leap_year(2017))
        self.assertFalse(calendar.is_leap_year(2018))
        self.assertFalse(calendar.is_leap_year(2019))

    def is_trading_day(self):
        self.assertFalse(calendar.is_bank_closed(datetime(2021, 1, 1))) # New Year's day observed, but we mocked the method
        self.assertTrue(calendar.is_bank_closed(datetime(2021, 3, 3))) # Wednesday
        self.assertFalse(calendar.is_bank_closed(datetime(2021, 3, 6))) # Saturday


if __name__ == '__main__':
    unittest.main()
