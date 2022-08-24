import sqlite3
import Model.EmployeeModel
from tkinter import messagebox as msg
import pyodbc as odb


class EmployeeDB:

    def __init__(self, employee: Model.EmployeeModel = None):
        self.Employee = employee

        self.connectionObject = odb.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=MARZIEH;"
            "Database=SematecLearningManagementSystem;"
            # "UID = sa"
            # "PWD = 123"
            "Trusted_Connection=yes"
        )

    def readEmployeeList(self):
        result = []
        cursor = self.connectionObject.cursor()
        cursor.execute('EXEC dbo.ReadListEmployee')
        for row in cursor:
            result.append(f'{row[0]} : {row[1]}')

        return result

    def insertEmployee(self):
        pass

    # def getEmployeeList(self):
    #     #  SQLite -----------------------------------------------------------------
    #     dbName = './DB/Sematec.db'
    #     query = 'SELECT Employee.PersonID , Person.FirstName , Person.LastName FROM Employee ' \
    #             'INNER JOIN Person ON Employee.PersonID=Person.ID'
    #
    #     try:
    #         with sqlite3.Connection(dbName) as connection:
    #             cursor = connection.cursor()
    #             cursor.execute(query)
    #             a = cursor.fetchall()
    #             connection.commit()
    #             return a
    #     except ConnectionError:
    #         pass
    #
    #     finally:
    #         connection.close()
    #
    # def getDepartmentList(self):
    #     dbName = './DB/Sematec.db'
    #     query = 'SELECT ID, DepartmentName FROM Department'
    #
    #     try:
    #         with sqlite3.Connection(dbName) as connection:
    #             cursor = connection.cursor()
    #             cursor.execute(query)
    #             a = cursor.fetchall()
    #             connection.commit()
    #             return a
    #     except ConnectionError:
    #         pass
    #
    #     finally:
    #         connection.close()
    #
    # def insertEmployee(self):
    #     dbName = './DB/Sematec.db'
    #     queryPerson = 'INSERT INTO Person(FirstName, LastName, NationalCode, Sex, Birthdate, Email, Mobile, Address,' \
    #                   'Education)' \
    #                   'VALUES(?,?,?,?,?,?,?,?,?)'
    #     paramsPerson = (self.Employee.FirstName, self.Employee.LastName, self.Employee.NationalCode,
    #                     self.Employee.Sex, self.Employee.Birthdate, self.Employee.Email, self.Employee.Mobile,
    #                     self.Employee.Address, self.Employee.Education)
    #     queryEmployee = 'INSERT INTO Employee(PersonID, ManagerID, Hiredate, departmentID)VALUES(?, ?, ?, ?)'
    #
    #     try:
    #         with sqlite3.Connection(dbName) as connection:
    #             cursor = connection.cursor()
    #             cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #             print('Tables:')
    #             print(cursor.fetchall())
    #             cursor.execute(queryPerson, paramsPerson)
    #             lastRowID = cursor.lastrowid
    #             paramsEmployee = (lastRowID, self.Employee.ManagerCode, self.Employee.Hiredate,
    #                               self.Employee.DepartmentID)
    #             cursor.execute(queryEmployee, paramsEmployee)
    #             connection.commit()
    #             msg.showinfo('Database', 'Added Successfully.')
    #     except ConnectionError:
    #         msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)
    #
    #     finally:
    #         connection.close()
