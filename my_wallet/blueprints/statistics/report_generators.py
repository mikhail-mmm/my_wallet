import datetime

from my_wallet.blueprints.statistics.custom_types import ReportData


def generate_biggest_expenses_report(
    date_from: datetime.date,
    date_to: datetime.date,
    wallets_ids: list[int],
) -> ReportData:
    return ReportData(
        columns=["date", "Test1", "Test2"],
        data=[
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
        ],
    )


def generate_expenses_by_weekday_report(
    date_from: datetime.date,
    date_to: datetime.date,
    wallets_ids: list[int],
) -> ReportData:
    return ReportData(
        columns=["date", "Test1", "Test2"],
        data=[
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
        ],
    )


def generate_expenses_by_week_report(
    date_from: datetime.date,
    date_to: datetime.date,
    wallets_ids: list[int],
) -> ReportData:
    return ReportData(
        columns=["date", "Test1", "Test2"],
        data=[
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
        ],
    )


def generate_expenses_by_type_report(
    date_from: datetime.date,
    date_to: datetime.date,
    wallets_ids: list[int],
) -> ReportData:
    return ReportData(
        columns=["date", "Test1", "Test2"],
        data=[
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
        ],
    )


def generate_weekly_balance_report(
    date_from: datetime.date,
    date_to: datetime.date,
    wallets_ids: list[int],
) -> ReportData:
    return ReportData(
        columns=["date", "Test1", "Test2"],
        data=[
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
            [datetime.datetime(2022, 4, 3), 5, 1],
        ],
    )
