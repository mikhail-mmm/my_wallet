import datetime


def is_report_range_valid(date_from: datetime.date, date_to: datetime.date) -> bool:
    return date_to <= date_from
