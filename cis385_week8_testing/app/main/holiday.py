
class Holiday:
    def is_federal_holiday(self, date):
        return self.is_new_year_observed(date)

    def is_new_year(self, datetime):
        return datetime.month == 1 and datetime.day == 1

    def is_new_year_observed(self, date):
        if self.is_new_year(date):
            return True
        if date.month == 12 and date.day == 31 and date.weekday() == 4:  # Friday before a Saturday New Year
            return True
        if date.month == 1 and date.day == 2 and date.weekday() == 0:  # Monday after a Sunday New Year
            return True
        return False
