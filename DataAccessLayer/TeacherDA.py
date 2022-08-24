import sqlite3
import Model.StudentModel
from tkinter import messagebox as msg
import pyodbc as odb


class TeacherDB:

    def __init__(self, teacher: Model.TeacherModel = None):
        self.Teacher = teacher

        self.connectionObject = odb.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=MARZIEH;"
            "Database=SematecLearningManagementSystem;"
            # "UID = sa"
            # "PWD = 123"
            "Trusted_Connection=yes"
        )

    def readTeacherList(self):
        result = []
        cursor = self.connectionObject.cursor()
        cursor.execute('EXEC dbo.ReadListTeacher')
        for row in cursor:
            result.append(f'{row[0]} : {row[1]}')

        return result

    def insertTeacher(self):
        pass

        #  SQLite -----------------------------------------------------------------

        # dbName = './DB/Sematec.db'
        # queryPerson = 'INSERT INTO Person(FirstName,LastName,NationalCode,Sex,Birthdate,Email,Mobile,Address, ' \
        #               'Education)VALUES(?,?,?,?,?,?,? ?,?)'
        # paramsPerson = (self.Teacher.FirstName, self.Teacher.LastName, self.Teacher.NationalCode,
        #                 self.Teacher.Sex, self.Teacher.Birthdate, self.Teacher.Email, self.Teacher.Mobile,
        #                 self.Teacher.Address, self.Teacher.Education)
        # queryTeacher = 'INSERT INTO Teacher(PersonID, CardNumber)VALUES(?,?)'
        #
        # try:
        #     with sqlite3.Connection(dbName) as connection:
        #         cursor = connection.cursor()
        #         # cursor.execute("SELECT name FROM sqlite_master WHERE   type='table';")
        #         # print('Tables:')
        #         # print(cursor.fetchall())
        #         cursor.execute(queryPerson, paramsPerson)
        #         lastRowID = cursor.lastrowid
        #         paramsTeacher = (lastRowID, self.Teacher.CardNumber)
        #         cursor.execute(queryTeacher, paramsTeacher)
        #         connection.commit()
        #         msg.showinfo('Database', 'Added Successfully.')
        # except ConnectionError:
        #     msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)
        #
        # finally:
        #     connection.close()
