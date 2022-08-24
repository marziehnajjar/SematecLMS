import sqlite3
import Model.DepartmentModel
from tkinter import messagebox as msg
import pyodbc as odb


class DepartmentDB:
    def __init__(self, department: Model.Department = None):
        self.Department = department

    def insertDepartment(self):
        #  SQLite -----------------------------------------------------------------
        dbName = './DB/Sematec.db'
        queryDepartment = 'INSERT INTO Department(DepartmentName,Description)VALUES(?,?)'
        paramsDepartment = (self.Department.DepartmentName, self.Department.Description)

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                cursor.execute(queryDepartment, paramsDepartment)
                connection.commit()
                msg.showinfo('Database', 'Added Successfully.')
        except ConnectionError:
            msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)

        finally:
            connection.close()
