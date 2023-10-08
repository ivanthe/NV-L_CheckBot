from openpyxl.workbook import Workbook

from pages.data_methods import DataMethods
from pages.xlsx_resulting_table_methods import ResultingTableMethods


def test_debug():
    tab = [['Медкомплекс АВК', 'Термостат НТ-120', 25860],
           ['СКТБ', 'ГП-20 СПУ', 33060],
           ['СКТБ', 'ГП-10 СПУ', 33560],
           ['Медкомплекс АВК', 'ГП-10 СПУ', 20250],
           ['Медкомплекс АВК', 'ГП-20 СПУ', 31250],
           ['НВ-Лаб', 'ГП-10 СПУ', 29680],
           ['НВ-Лаб', 'Термостат НТ-120', 25860]]

    for row in tab:
        if row[0] == 'НВ-Лаб':
            print(row[1], ' стоит ', row[2], ' руб.')

def test_sort():
    data_one = [['Медкомплекс АВК', 'Термостат НТ-120', 25860],
                ['СКТБ', 'ГП-20 СПУ', 33060],
                ['СКТБ', 'ГП-10 СПУ', 33560],
                ['Медкомплекс АВК', 'ГП-10 СПУ', 20250],
                ['Медкомплекс АВК', 'ГП-20 СПУ', 31250],
                ['НВ-Лаб', 'ГП-10 СПУ', 29680],
                ['НВ-Лаб', 'Термостат НТ-120', 25860]]


    process = DataMethods(data_one)
    data = process.sort_list(data_one)
    print("")

    def takeSecond(elem):
        return elem[1]
    def takeThird(elem):
        return elem[2]


    def get_number_of_items_in_list(cell_value, current_data):
        b = 0
        for cell in current_data:
            if cell_value in cell:
                b += 1
        return b

    def get_list_of_tempory_data(list_size, current_data):
        data = []
        for c in range(0, list_size):
            data.append(current_data.pop(0))
        return data, current_data

    data.sort(key=takeSecond)
    for row in data:
        print(row)

    def get_resulting_data(resulting_data, current_data):
        data = resulting_data
        for row in current_data:
            data.append(row)
        return data

    data_temp = data
    resulting_data = []

    while data_temp != []:
        value = data_temp[0][1]
        value_qty = get_number_of_items_in_list(value, data_temp)
        tempory_data, data_temp = get_list_of_tempory_data(value_qty, data_temp)
        tempory_data.sort(key=takeThird)
        resulting_data = get_resulting_data(resulting_data, tempory_data)
        tempory_data.clear()

    print('Финальная таблица')
    for row in resulting_data:
        print(row)

    result_workbook = Workbook()
    result_list = result_workbook.active

    xlsx_process = ResultingTableMethods(result_list)
    xlsx_process.create_first_row_of_resulting_table(result_list, resulting_data)
    xlsx_process.format_the_resulting_table(result_list)

    result_workbook.save('debug.xlsx')

def test_get_price():
    def change_str_to_num(price_from_site):
        current_price = ''

        for char in price_from_site:
            if char.isdigit() or char == ',' or char == '-':
                current_price = current_price + char
        if '-00' in current_price:
            current_price = current_price.replace('-00', '')
        if ',00' in current_price:
            current_price = current_price.replace(',00', '')
        return current_price


    price_from_site = 'asdfsdfa 20 000,00 adf'
    price = change_str_to_num(price_from_site)

    print(price)