import datetime


def is_report_range_valid(date_from: datetime.date, date_to: datetime.date) -> bool:
    return date_to <= date_from


if __name__ == '__main__':
    date_from = datetime.date(2023, 2, 1)
    date_to = datetime.date(2023, 1, 1)
    assert is_report_range_valid(date_from, date_to)
