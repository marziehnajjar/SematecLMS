from Model import *
from DataAccessLayer import *


class RegisterationVD:
    def __init__(self, registeration: RegisterationModel.Registeration):
        self.Registeration = registeration

    def validationForm(self):
        error = 0

        if error == 0:
            registerdb = RegisterationDB(self.registeration)
            registerdb.insertRow()
