from pages.data_processing import DataProcessing


class DataMethods(DataProcessing):
    @staticmethod
    def get_number_of_items_in_list(cell_value, current_data):
        b = 0
        for cell in current_data:
            if cell_value in cell:
                b += 1
        return b



    @staticmethod
    def get_list_of_temporary_data(list_size, current_data):
        data = []
        for c in range(0, list_size):
            data.append(current_data.pop(0))
        return data, current_data

    @staticmethod
    def get_resulting_data(resulting_data, temporary_data, target_price):
        data = resulting_data
        for row in temporary_data:
            try:
                price_deviation = (row[4] - target_price)*100/target_price

            except ZeroDivisionError:
                row.append(0)
            else:
                row.append(price_deviation)
            data.append(row)

        return data

    @staticmethod
    def get_final_data(resulting_data):
        data = []
        for row in resulting_data:
            site_title = row[5].split('://')[-1].split('/')[0]
            data.append([row[0], site_title, row[3], row[4], row[6], row[5], row[1]])
        return data

    @staticmethod
    def sort_list(data):
        data_processing = DataMethods(data)

        # noinspection PyPep8Naming
        def takeSecond(elem):
            return elem[1]

        # noinspection PyPep8Naming
        def takeThird(elem):
            return elem[4]

        def find_target_price(temporary_data):
            target_price = 0

            for cell in temporary_data:
                if "НВ-Лаб" in cell:
                    target_price = cell[4]
                    break
            return target_price


        data.sort(key=takeSecond)


        data_temp = data
        resulting_data = []

        while data_temp != []:
            value = data_temp[0][1]
            #считаем количество полей со значением value
            value_qty = data_processing.get_number_of_items_in_list(value, data_temp)
            # создаем временную таблицу, в которой будут только поля со значением value
            # и удаляем все поля из исходной таблице где есть значение value
            temporary_data, data_temp = data_processing.get_list_of_temporary_data(value_qty, data_temp)
            # сортируем временную таблицу по цене
            temporary_data.sort(key=takeThird)
            # ищем минимальную цену соответсвующую цене на сайте НВ-Лаб
            target_price = find_target_price(temporary_data)
            resulting_data = data_processing.get_resulting_data(resulting_data, temporary_data, target_price)
            for c in resulting_data:
                print(c)
            temporary_data.clear()

        final_data = data_processing.get_final_data(resulting_data)
        print(final_data)

        return final_data
