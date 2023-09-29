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
    def get_resulting_data(resulting_data, current_data):
        data = resulting_data
        for row in current_data:
            data.append(row)
        return data

    @staticmethod
    def sort_list(data):
        data_processing = DataMethods(data)

        # noinspection PyPep8Naming
        def takeSecond(elem):
            return elem[1]

        # noinspection PyPep8Naming
        def takeThird(elem):
            return elem[2]

        data.sort(key=takeSecond)


        data_temp = data
        resulting_data = []

        while data_temp != []:
            value = data_temp[0][1]
            value_qty = data_processing.get_number_of_items_in_list(value, data_temp)
            temporary_data, data_temp = data_processing.get_list_of_temporary_data(value_qty, data_temp)
            temporary_data.sort(key=takeThird)
            resulting_data = data_processing.get_resulting_data(resulting_data, temporary_data)
            temporary_data.clear()

        return resulting_data
