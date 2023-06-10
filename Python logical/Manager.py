import json
import random
from datetime import datetime
from Data_layer import *
from Employee import Employee

class Manager(Employee):
    def __init__(self, employee_data):
        super().__init__(employee_data["employee_id"], employee_data["name"],
                         employee_data["phone"], employee_data["email"], employee_data["role"])

    def view_employees(self):
        Employee.view_employees()

    