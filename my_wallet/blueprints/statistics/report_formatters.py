from io import BytesIO

import xlsxwriter
from flask import Response, render_template, send_file

from my_wallet.blueprints.statistics.custom_types import ReportData
from my_wallet.blueprints.statistics.forms import StatReportForm


def generate_html_response(report_data: ReportData, form: StatReportForm) -> Response | str:
    return render_template("stat_report_form.html", form=form, report_data=report_data)


def generate_xlsx_response(report_data: ReportData, form: StatReportForm) -> Response | str:
    header_row_num = 0

    xlsx_file_io = BytesIO()
    workbook = xlsxwriter.Workbook(xlsx_file_io, options={"in_memory": True})
    bold = workbook.add_format({'bold': True})
    worksheet = workbook.add_worksheet()
    for column_num, column_name in enumerate(report_data.columns):
        worksheet.write(header_row_num, column_num, column_name, bold)
    for data_row_num, data_item in enumerate(report_data.data):
        for data_item_num, item in enumerate(data_item):
            worksheet.write(header_row_num + data_row_num + 1, data_item_num, item)
    workbook.close()

    xlsx_file_data = xlsx_file_io.getvalue()

    return send_file(BytesIO(xlsx_file_data), download_name="report.xlsx")


def generate_pdf_response(report_data: ReportData, form: StatReportForm) -> Response | str:
    pass
