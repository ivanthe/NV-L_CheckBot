from data.data import FontStyle, BorderStyle, ResultingTableFields


def first_row_style():
    yield FontStyle(
        font_size=14,
        font_bold=True,
        font_color='FFFF00'
    )


def nv_lab_row_style():
    yield FontStyle(
        font_size=14,
        font_bold=True,
        font_color='00FFFF'
    )


def default_row_style():
    yield FontStyle(
        font_size=12,
        font_bold=False,
        font_color='FFFFFF'
    )


def error_row_style():
    yield FontStyle(
        font_size=12,
        font_bold=False,
        font_color='FF0000'
    )


def first_row_border_style():
    yield BorderStyle(
        cell_width=20,
        cell_height=40,
        cell_border_style="thick",
        cell_border_color="000000",
        cell_alignment_horizontal='center',
        cell_alignment_vertical='center'
    )


def default_row_border_style():
    yield BorderStyle(
        cell_width=20,
        cell_height=40,
        cell_border_style="thin",
        cell_border_color="000000",
        cell_alignment_horizontal='center',
        cell_alignment_vertical='center'
    )


def resulting_table_fields_name():
    yield ResultingTableFields(
        field_1='code',
        field_2='Company_name',
        field_3='Good_category',
        field_4='Goods_name',
        field_5='Price',
        field_6='Price_deviation',
    )
