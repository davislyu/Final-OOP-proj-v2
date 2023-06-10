import json
import os


class DataFactory:

    @staticmethod
    def get_data(file_path):
        # This function reads and retrieves data from a JSON file.
        # It takes the file path as input and returns the loaded data.
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def save_data(file_path, data):
        # This function saves data to a JSON file.
        # It takes the file path and data to be saved as inputs.
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)


class Data_Employee:
    @staticmethod
    def get_employees():
        # This function gets the employee data.
        # It retrieves the employee data and returns it.
        data_path = os.path.join("Databases", "employees.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_employees(employees):
        # This function saves the employee data.
        # It takes the employee data as input and saves it.
        data_path = os.path.join("Databases", "employees.json")
        DataFactory.save_data(data_path, employees)


class Data_Stock:
    @staticmethod
    def get_ingredients():
        # This function retrieves the ingredient data.
        # It gets the ingredient data and returns it.
        data_path = os.path.join("Databases", "Stock.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_ingredients(ingredients):
        # This function saves the ingredient data.
        # It takes the ingredient data as input and saves it.
        data_path = os.path.join("Databases", "Stock.json")
        DataFactory.save_data(data_path, ingredients)


class Data_Menu:
    @staticmethod
    def display_menu():
        # This function displays the menu data.
        # It retrieves and returns the menu data.
        data_path = os.path.join("Databases", "menu.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_to_menu(menu_data):
        # This function saves the updated menu data.
        # It takes the updated menu data as input and saves it.
        data_path = os.path.join("Databases", "menu.json")
        existing_data = DataFactory.get_data(data_path)
        existing_data['menu_items'] = menu_data['menu_items']
        DataFactory.save_data(data_path, existing_data)


class Data_Table:
    @staticmethod
    def get_tables():
        # This function gets the table data.
        # It retrieves and returns the table data.
        data_path = os.path.join("Databases", "tables.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_tables(tables):
        # This function saves the table data.
        # It takes the table data as input and saves it.
        data_path = os.path.join("Databases", "tables.json")
        DataFactory.save_data(data_path, tables)


class Data_OrderHistory:
    @staticmethod
    def get_order_history():
        # This function gets the order history data.
        # It retrieves and returns the order history data.
        data_path = os.path.join("Databases", "order_history.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_order_history(order_history):
        # This function saves the order history data.
        # It takes the order history data as input and saves it.
        data_path = os.path.join("Databases", "order_history.json")
        DataFactory.save_data(data_path, order_history)
