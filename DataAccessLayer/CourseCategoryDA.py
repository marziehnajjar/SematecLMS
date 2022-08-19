import sqlite3
import Model.CourseCategoryModel
from tkinter import messagebox as msg


class CourseCategoryDB:
    def __init__(self, courseCategory: Model.CourseCategoryModel = None):
        self.CourseCategory = courseCategory

    def insertCourseCategory(self):
        dbName = './DB/Sematec.db'
        queryCourseCategory = 'INSERT INTO CourseCategory(CourseCategoryName)VALUES(?)'
        paramsCourseCategory = (self.CourseCategory.CourseCategoryName,)

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                cursor.execute(queryCourseCategory, paramsCourseCategory)
                connection.commit()
                msg.showinfo('Database', 'Added Successfully.')
        except ConnectionError:
            msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)
        finally:
            connection.close()
