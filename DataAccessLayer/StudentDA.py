# import sqlite3
import Model.StudentModel
from tkinter import messagebox as msg
import pyodbc as odb


class StudentDB:

    def __init__(self, student: Model.StudentModel = None):
        self.Student = student

        self.connectionObject = odb.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=MARZIEH;"
            "Database=SematecLearningManagementSystem;"
            # "UID = sa"
            # "PWD = 123"
            "Trusted_Connection=yes"
        )

    def insertStudent(self):
            cursor = self.connectionObject.cursor()
            spQuery = 'EXEC dbo.AddStudent ' \
                      '@FirstName = ?,' \
                      '@LastName = ?,'\
                      '@NationalCode = ?,'\
                      '@Sex = ?,'\
                      '@Birthdate = ?,'\
                      '@Email = ?,'\
                      '@Mobile = ?, ' \
                      '@Country =?,' \
                      '@Province = ?,' \
                      '@City = ?,' \
                      '@Street = ?,' \
                      '@PostalCode = ?,' \
                      '@StudentTypeID = ?'
            params = (self.Student.FirstName, self.Student.LastName, self.Student.NationalCode, self.Student.Sex,
                      self.Student.Birthdate, self.Student.Email, self.Student.Mobile, self.Student.Country,
                      self.Student.Province, self.Student.City, self.Student.Street, self.Student.Postalcode,
                      self.Student.Type)
            cursor.execute(spQuery, params)
            self.connectionObject.commit()

    def readEducationFiels(self):
        result = []
        cursor = self.connectionObject.cursor()
        cursor.execute('EXEC dbo.ReadEducationFields')
        for row in cursor:
            result.append(f'{row[0]} : {row[1]}')

        return result

    def addEducationPerson(self, EducationDegree, EducationfieldID):
        result = []
        cursor = self.connectionObject.cursor()
        cursor.execute('EXEC dbo.ReadLastPersonID')
        for row in cursor:
            PersonID = row[0]
        PersonID += 1
        cursor = self.connectionObject.cursor()
        spQuery = 'EXEC dbo.AddEducationPerson ' \
                  '@PersonID = ?,' \
                  '@EducationDegree = ?,' \
                  '@EducationFieldID = ?'
        params = (PersonID, EducationDegree, EducationfieldID)
        cursor.execute(spQuery, params)
        self.connectionObject.commit()

    def readStudentList(self):
        result = []
        cursor = self.connectionObject.cursor()
        cursor.execute('EXEC dbo.ReadListStudent')
        for row in cursor:
            result.append(f'{row[0]} : {row[1]}')

        return result

    def readStudent(self, id):
        cursor = self.connectionObject.cursor()
        cursor.execute('EXEC dbo.ReadStudent @StudentID=' + id)
        for row in cursor:
            return row

    def readStudentEducation(self, id):
        result = []
        cursor = self.connectionObject.cursor()
        cursor.execute('EXEC dbo.ReadStudentEducation @StudentID=' + id)
        for row in cursor:
            result.append(str(row[0]) + ':' + row[1])
        return result

    def deleteStudent(self, id):
        cursor = self.connectionObject.cursor()
        cursor.execute('EXEC dbo.DeleteStudent @StudentID=' + id)
        cursor.commit()

    def updateStudent(self):
        cursor = self.connectionObject.cursor()
        spQuery = 'EXEC dbo.UpdateStudent ' \
                  '@StudentID = ?,' \
                  '@FirstName = ?,' \
                  '@LastName = ?,' \
                  '@NationalCode = ?,' \
                  '@Sex = ?,' \
                  '@Birthdate = ?,' \
                  '@Email = ?,' \
                  '@Mobile = ?, ' \
                  '@Country =?,' \
                  '@Province = ?,' \
                  '@City = ?,' \
                  '@Street = ?,' \
                  '@PostalCode = ?,' \
                  '@StudentTypeID = ?'
        params = (self.Student.StudentID, self.Student.FirstName, self.Student.LastName, self.Student.NationalCode,
                  self.Student.Sex, self.Student.Birthdate, self.Student.Email, self.Student.Mobile,
                  self.Student.Country, self.Student.Province, self.Student.City, self.Student.Street,
                  self.Student.Postalcode, self.Student.Type)
        cursor.execute(spQuery, params)
        self.connectionObject.commit()

    def readStudentTypeList(self):
        result = []
        cursor = self.connectionObject.cursor()
        cursor.execute('EXEC dbo.ReadStudentTypeList')
        for row in cursor:
            result.append(row[0])

        return result

#  SQLite -----------------------------------------------------------------
        # dbName = './DB/Sematec.db'
        # # queryPerson = 'INSERT INTO Person(FirstName,LastName,NationalCode,Sex,Birthdate,Email,Mobile,Address,Education)' \
        # #               'VALUES(?,?,?,?,?,?,?,?,?)'
        # # paramsPerson = (self.Student.FirstName, self.Student.LastName, self.Student.NationalCode, self.Student.Sex,
        # #                 self.Student.Birthdate, self.Student.Email, self.Student.Mobile, self.Student.Address,
        # #                 self.Student.Education)
        # queryStudent = 'INSERT INTO Student(PersonID,Type)VALUES(?,?)'
        #
        # try:
        #     with sqlite3.Connection(dbName) as connection:
        #         cursor = connection.cursor()
        #         # result = cursor.execute(queryPerson, paramsPerson)
        #         lastRowID = cursor.lastrowid
        #         paramsStudent = (lastRowID, self.Student.Type)
        #         cursor.execute(queryStudent, paramsStudent)
        #         connection.commit()
        #         msg.showinfo('Database', 'Added Successfully.')
        # except ConnectionError:
        #     msg.showerror('Database', 'Unexpected failure.Error: ' + ConnectionError.strerror)
        #
        # finally:
        #     connection.close()
