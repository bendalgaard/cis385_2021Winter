
from app.main.holiday import Holiday


def is_leap_year(year):
    if year < 1900:
        raise ValueError()

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0


def is_bank_closed(date):
    return Holiday.is_new_year_observed(date=date) or date.weekday() == 5 or date.weekday() == 6
