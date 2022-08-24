import sqlite3
import Model.StudentModel
from tkinter import messagebox as msg
import pyodbc as odb


class UserDB:
    def __init__(self, user: Model.UserModel = None):
        self.User = user

    def insertRow(self):
        #  SQLite -----------------------------------------------------------------
        dbName = './DB/Sematec.db'
        query = 'INSERT INTO User(FirstName,LastName,UserName,Password,Admin)' \
                'VALUES(?,?,?,?,?)'
        params = (self.User.FirstName, self.User.LastName, self.User.UserName, self.User.Password, self.User.Admin)

        try:
            with sqlite3.Connection(dbName) as connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                msg.showinfo('Database', 'Added Successfully.')
        except ConnectionError:
            msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)

        finally:
            connection.close()

    def getRolesList(self):
        dbName = './DB/Sematec.db'
        query = 'SELECT ID,FirstName FROM User'

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
