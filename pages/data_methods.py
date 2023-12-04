from pages.data_processing import DataProcessing


class DataMethods(DataProcessing):

    @staticmethod
    def get_number_of_items_in_list(cell_value, current_data) -> int:
        b = 0
        for cell in current_data:
            if cell_value in cell:
                b += 1
        return b

    @staticmethod
    def get_list_of_temporary_data(list_size, current_data) -> tuple:
        data = []
        for c in range(0, list_size):
            data.append(current_data.pop(0))
        return data, current_data

    @staticmethod
    def get_resulting_data(resulting_data, temporary_data, target_price) -> list:
        data = resulting_data
        for row in temporary_data:
            try:
                price_deviation = (row[4] - target_price) * 100 / target_price
                price_deviation = round(price_deviation, 1)

            except ZeroDivisionError:
                row.append(0)
            else:
                row.append(price_deviation)
            data.append(row)
        return data

    @staticmethod
    def get_final_data(resulting_data) -> list:
        data = []
        for row in resulting_data:
            site_title = row[5].split('://')[-1].split('/')[0]
            data.append([row[0], site_title, row[1], row[3], row[4], row[6], row[5]])
        return data

    @staticmethod
    def find_target_price(temporary_data) -> float:
        target_price = 0

        for cell in temporary_data:
            if "НВ-Лаб" in cell:
                target_price = cell[4]
                break
        return target_price

    def sort_list(self) -> list:

        self.data_from_pages.sort(key=lambda sort_column: sort_column[1])

        data_temp = self.data_from_pages
        resulting_data = []

        while data_temp != []:
            value = data_temp[0][1]

            # считаем количество полей со значением value
            value_qty = DataMethods.get_number_of_items_in_list(value, data_temp)

            # создаем временную таблицу, в которой будут только поля со значением value
            # и удаляем все поля из исходной таблице где есть значение value
            temporary_data, data_temp = DataMethods.get_list_of_temporary_data(value_qty, data_temp)

            # сортируем временную таблицу по цене
            temporary_data.sort(key=lambda sort_column: sort_column[4])

            # ищем минимальную цену соответсвующую цене на сайте НВ-Лаб
            target_price = DataMethods.find_target_price(temporary_data)
            resulting_data = DataMethods.get_resulting_data(resulting_data, temporary_data, target_price)
            temporary_data.clear()

        final_data = DataMethods.get_final_data(resulting_data)

        return final_data
