from openpyxl.styles import PatternFill, Font, Alignment, Border, Side


class XlxsMethods:

    def __init__(self, xlxs_list):
        self.xlxs_list = xlxs_list

    def paint_first_row(self, color):

        for row in self.xlxs_list.iter_rows(min_row=1, max_col=4, max_row=1):
            for cell in row:
                cell.fill = PatternFill('solid', fgColor=color)
                cell.font = Font(size=14, bold=True)

        self.xlxs_list.column_dimensions['A'].width = 30
        self.xlxs_list.column_dimensions['B'].width = 40
        self.xlxs_list.column_dimensions['C'].width = 20
        self.xlxs_list.column_dimensions['D'].width = 80
        self.xlxs_list.row_dimensions[1].height = 40

        line = Side(border_style="thick", color="000000")

        for cell in self.xlxs_list[1]:
            cell.alignment = Alignment(horizontal='center', vertical='center')
            cell.border = Border(top=line, bottom=line, left=line, right=line)
