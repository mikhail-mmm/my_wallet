import dataclasses


@dataclasses.dataclass(frozen=True, slots=True, kw_only=True)
class ReportData:
    columns: list[str]
    data: list[list]
