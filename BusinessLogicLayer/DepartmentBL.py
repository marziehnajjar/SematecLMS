from Model import *
from DataAccessLayer import *


class DepartmentVD:
    def __init__(self, department: DepartmentModel.Department):
        self.Department = department

    def validationForm(self):
        error = 0

        if error == 0:
            departmentdb = DepartmentDB(self.department)
            departmentdb.insertDepartment()
