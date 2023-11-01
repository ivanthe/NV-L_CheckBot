import openpyxl
import xlwt



def checking():
    select_dict = openpyxl.load_workbook('select_dict.xlsx')
    datafile = openpyxl.load_workbook('datafile.xlsx')
    select_dict_sheet = select_dict.active
    datafile_sheet = datafile.active
    data = []

    for c in range(1, select_dict_sheet.max_row + 1):
        data.append(select_dict_sheet.cell(row=c, column=1).value)

    for i in range(2, datafile_sheet.max_row + 1):
        url = datafile_sheet.cell(row=i, column=5).value
        site_title = url.split('://')[-1].split('/')[0]
        if 'www.' in site_title:
            site_title = site_title.split('www.')[-1]

        if site_title not in data:
            print(f'Для сайта {site_title} нет локатора.')





if __name__ == '__main__':
    checking()