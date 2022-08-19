import sqlite3
import Model.CourseCategoryModel
from tkinter import messagebox as msg


class CourseDB:

    def __init__(self, course: Model.CourseModel = None):
        self.Course = course

    def insertCourse(self):
        dbName = './DB/Sematec.db'
        queryCourse = 'INSERT INTO Course(CoursecategoryID,CourseName,Duration,Description)VALUES(?,?,?,?)'
        paramsCourse = (self.Course.CoursecategoryID, self.Course.CourseName, self.Course.Duration,
                        self.Course.Description)

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                cursor.execute(queryCourse, paramsCourse)
                connection.commit()
                msg.showinfo("Added Successfully.")
        except ConnectionError:
            msg.showerror("Unexpected failure. Error: " + ConnectionError.strerror)

        finally:
            connection.close()

    def getCourseCategoryList(self):
        dbName = './DB/Sematec.db'
        query = 'SELECT ID,CourseCategoryName FROM CourseCategory'

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                # a = cursor.fetchall()
                connection.commit()
                # return a
        except ConnectionError:
            pass

        finally:
            connection.close()
