import json
import random
from datetime import datetime
from Data_layer import *
from Employee import Employee
import Table

class Hostess(Employee):
    def __init__(self, employee_data):
        """
        Initialize a Hostess object.
        """
        super().__init__(employee_data["employee_id"], employee_data["name"],
                         employee_data["phone"], employee_data["email"], employee_data["role"])

    def reserve_table(self):
        """
        Reserve a table.
        """
        Table.reserve_table()
