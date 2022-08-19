import sqlite3
import Model.RegisterationModel
from tkinter import messagebox as msg


class RegisterationDB:

    def __init__(self, registeration: Model.RegisterationModel = None):
        self.Registeration = registeration

    def getTeacherList(self):
        dbName = './DB/Sematec.db'
        query = 'SELECT Teacher.PersonID , Person.FirstName , Person.LastName FROM Teacher ' \
                'INNER JOIN Person ON Teacher.PersonID=Person.ID'

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                a = cursor.fetchall()
                connection.commit()
                return a
        except ConnectionError:
            pass
            ''' 
            the pass is the no-operation statement. This class doesn't define any methods or attributes,
             but syntactically, there needs to be something in the definition, thus the pass statement. 
             This is a Python reserved word that just means move along, nothing to see here. It's a statement
              that does nothing, and it's a good placeholder when we're stubbing out functions or classes.  
            '''
        finally:
            connection.close()

    def getStudentList(self):
        dbName = './DB/Sematec.db'
        query = 'SELECT Student.PersonID , Person.FirstName , Person.LastName FROM Student ' \
                'INNER JOIN Person ON Student.PersonID=Person.ID'

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                a = cursor.fetchall()
                connection.commit()
                return a
        except ConnectionError:
            pass

        finally:
            connection.close()

    def getCourseList(self):
        dbName = './DB/Sematec.db'
        query = 'SELECT ID , CourseName FROM Course '

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                a = cursor.fetchall()
                connection.commit()
                return a
        except ConnectionError:
            pass

        finally:
            connection.close()

    def insertRow(self):
        dbName = './DB/Sematec.db'
        query = 'INSERT INTO StudentTeacherCourse(StudentID, CourseID, TeacherID, YearQuarter, Score)' \
                'VALUES(?, ?, ?, ?, ?)'
        params = (self.Registeration.StudentID, self.Registeration.CourseID, self.Registeration.TeacherID,
                  self.Registeration.YearQuarter, self.Registeration.Score)

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                result = cursor.execute(query, params)
                print(result)
                connection.commit()
                msg.showinfo('Database', 'Added Successfully.')
        except ConnectionError:
            msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)

        finally:
            connection.close()
