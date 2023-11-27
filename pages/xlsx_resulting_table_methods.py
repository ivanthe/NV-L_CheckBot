from data.styles import first_row_style, first_row_border_style, nv_lab_row_style, default_row_border_style, \
    default_row_style, error_row_style
from pages.xlsx_proccessing import XlsxProccessing


class ResultingTableMethods(XlsxProccessing):

    @staticmethod
    def create_first_row_of_resulting_table(result_list, data_from_pages):
        result_list.append(['code', 'Company_name', 'Goods_name', 'Price', 'Price_deviation'])
        for row in data_from_pages:
            result_list.append(row)

    def format_the_resulting_table(self, result_list):
        font_style = next(first_row_style())
        border_style = next(first_row_border_style())
        self.format_row(font_style, border_style, result_list[1])
        self.xlxs_list.column_dimensions['A'].width = border_style.cell_width * 0.75
        self.xlxs_list.column_dimensions['B'].width = border_style.cell_width * 1.75
        self.xlxs_list.column_dimensions['C'].width = border_style.cell_width * 1.5
        self.xlxs_list.column_dimensions['D'].width = border_style.cell_width
        self.xlxs_list.column_dimensions['E'].width = border_style.cell_width * 0.75
        self.xlxs_list.column_dimensions['F'].width = border_style.cell_width * 1.75
        self.xlxs_list.row_dimensions[1].height = border_style.cell_height

        for i in range(2, result_list.max_row+1):

            if result_list[i][1].value == 'www.nv-lab.ru' and result_list[i][3].value >= 0:
                font_style = next(nv_lab_row_style())
                border_style = next(default_row_border_style())
                self.format_row(font_style, border_style, result_list[i])
                if result_list[i][3].value == 0:
                    result_list[i][3].value = 'ПО ЗАПРОСУ'
            elif result_list[i][1].value != 'www.nv-lab.ru' and result_list[i][3].value >= 0:
                font_style = next(default_row_style())
                border_style = next(default_row_border_style())
                self.format_row(font_style, border_style, result_list[i])
                if result_list[i][3].value == 0:
                    result_list[i][3].value = 'ПО ЗАПРОСУ'
            elif result_list[i][3].value < 0:
                font_style = next(error_row_style())
                border_style = next(default_row_border_style())
                self.format_row(font_style, border_style, result_list[i])
                result_list[i][3].value = 'ОШИБКА'
                print(result_list[i][3].value)

            print(result_list[i][3].value)

            if int(result_list[i][4].value) < 0:
                self.format_cell(color='F08080', cell=result_list[i][4])
            elif int(result_list[i][4].value) > 0:
                self.format_cell(color='98FB98', cell=result_list[i][4])

        for i in range(2, result_list.max_row + 1):
            result_list[i][3].hyperlink = result_list[i][5].value

        result_list.delete_cols(6)




