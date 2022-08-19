import sqlite3
import Model.StudentModel
from tkinter import messagebox as msg


class StudentDB:

    def __init__(self, student: Model.StudentModel = None):
        self.Student = student

    def insertStudent(self):
        dbName = './DB/Sematec.db'
        # queryPerson = 'INSERT INTO Person(FirstName,LastName,NationalCode,Sex,Birthdate,Email,Mobile,Address,Education)' \
        #               'VALUES(?,?,?,?,?,?,?,?,?)'
        # paramsPerson = (self.Student.FirstName, self.Student.LastName, self.Student.NationalCode, self.Student.Sex,
        #                 self.Student.Birthdate, self.Student.Email, self.Student.Mobile, self.Student.Address,
        #                 self.Student.Education)
        queryStudent = 'INSERT INTO Student(PersonID,Type)VALUES(?,?)'

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                # result = cursor.execute(queryPerson, paramsPerson)
                lastRowID = cursor.lastrowid
                paramsStudent = (lastRowID, self.Student.Type)
                cursor.execute(queryStudent, paramsStudent)
                connection.commit()
                msg.showinfo('Database', 'Added Successfully.')
        except ConnectionError:
            msg.showerror('Database', 'Unexpected failure.Error: ' + ConnectionError.strerror)

        finally:
            connection.close()
