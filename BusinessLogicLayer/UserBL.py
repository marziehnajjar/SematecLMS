from Model import *
from DataAccessLayer import *


class UserVD:
    def __init__(self, user: UserModel.User):
        self.User = user

    def validationForm(self):
        error = 0

        if error == 0:
            userdb = UserDB(self.user)
            userdb.insertRow()

