import sqlite3
import Model.StudentModel
from tkinter import messagebox as msg


class TeacherDB:

    def __init__(self, teacher: Model.TeacherModel = None):
        self.Teacher = teacher

    def insertTeacher(self):
        dbName = './DB/Sematec.db'
        queryPerson = 'INSERT INTO Person(FirstName,LastName,NationalCode,Sex,Birthdate,Email,Mobile,Address, ' \
                      'Education)VALUES(?,?,?,?,?,?,? ?,?)'
        paramsPerson = (self.Teacher.FirstName, self.Teacher.LastName, self.Teacher.NationalCode,
                        self.Teacher.Sex, self.Teacher.Birthdate, self.Teacher.Email, self.Teacher.Mobile,
                        self.Teacher.Address, self.Teacher.Education)
        queryTeacher = 'INSERT INTO Teacher(PersonID, CardNumber)VALUES(?,?)'

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                # cursor.execute("SELECT name FROM sqlite_master WHERE   type='table';")
                # print('Tables:')
                # print(cursor.fetchall())
                cursor.execute(queryPerson, paramsPerson)
                lastRowID = cursor.lastrowid
                paramsTeacher = (lastRowID, self.Teacher.CardNumber)
                cursor.execute(queryTeacher, paramsTeacher)
                connection.commit()
                msg.showinfo('Database', 'Added Successfully.')
        except ConnectionError:
            msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)

        finally:
            connection.close()
