import unittest
from datetime import datetime

from app.main.holiday import Holiday


class TestCalendar(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_new_year_returns_true_for_newyears(self):
        holiday = Holiday()
        self.assertTrue(holiday.is_new_year(datetime(2021, 1, 1)))
        self.assertTrue(holiday.is_new_year(datetime(2022, 1, 1)))

    def test_is_new_year_observed_true_for_newyears(self):
        holiday = Holiday()
        self.assertTrue(holiday.is_new_year_observed(datetime(2021, 1, 1)))
        self.assertTrue(holiday.is_new_year_observed(datetime(2021, 12, 31)))

    def test_is_new_year_observed_false_for_wrong_newyears(self):
        holiday = Holiday()
        self.assertFalse(holiday.is_new_year(datetime(2020, 12, 31)))


if __name__ == '__main__':
    unittest.main()
