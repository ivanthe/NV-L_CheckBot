from data.styles import first_row_style, first_row_border_style, nv_lab_row_style, default_row_border_style, \
    default_row_style, error_row_style, resulting_table_fields_name
from pages.xlsx_proccessing import XlsxProccessing


class ResultingTableMethods(XlsxProccessing):

    @staticmethod
    def create_first_row_of_resulting_table(result_list, data_from_pages) -> None:
        fields = next(resulting_table_fields_name())
        result_list.append([fields.field_1, fields.field_2, fields.field_3,
                            fields.field_4, fields.field_5, fields.field_6])
        for row in data_from_pages:
            result_list.append(row)

    def format_the_resulting_table(self, result_list) -> None:
        font_style = next(first_row_style())
        border_style = next(first_row_border_style())
        self.format_row(font_style, border_style, result_list[1])
        self.xlxs_list.column_dimensions['A'].width = border_style.cell_width * 0.5
        self.xlxs_list.column_dimensions['B'].width = border_style.cell_width * 1.5
        self.xlxs_list.column_dimensions['C'].width = border_style.cell_width * 1.75
        self.xlxs_list.column_dimensions['D'].width = border_style.cell_width * 2
        self.xlxs_list.column_dimensions['E'].width = border_style.cell_width * 0.75
        self.xlxs_list.column_dimensions['F'].width = border_style.cell_width * 1
        self.xlxs_list.row_dimensions[1].height = border_style.cell_height

        for i in range(2, result_list.max_row+1):

            if result_list[i][1].value == 'www.nv-lab.ru' and result_list[i][4].value >= 0:
                font_style = next(nv_lab_row_style())
                border_style = next(default_row_border_style())
                self.format_row(font_style, border_style, result_list[i])
                if result_list[i][4].value == 0:
                    result_list[i][4].value = 'ПО ЗАПРОСУ'
            elif result_list[i][1].value != 'www.nv-lab.ru' and result_list[i][4].value >= 0:
                font_style = next(default_row_style())
                border_style = next(default_row_border_style())
                self.format_row(font_style, border_style, result_list[i])
                if result_list[i][4].value == 0:
                    result_list[i][4].value = 'ПО ЗАПРОСУ'
            elif result_list[i][4].value < 0:
                font_style = next(error_row_style())
                border_style = next(default_row_border_style())
                self.format_row(font_style, border_style, result_list[i])
                result_list[i][4].value = 'ОШИБКА'

            if int(result_list[i][5].value) < 0:
                self.format_cell(color='F08080', cell=result_list[i][5])
            elif int(result_list[i][5].value) > 0:
                self.format_cell(color='98FB98', cell=result_list[i][5])

        for i in range(2, result_list.max_row + 1):
            result_list[i][1].hyperlink = result_list[i][6].value

        result_list.delete_cols(7)
