from Model import *
from DataAccessLayer import *


class CourseVD:
    def __init__(self, course: CourseModel.Course):
        self.Course = course

    def validationForm(self):
        error = 0

        if error == 0:
            coursedb = CourseDB(self.course)
            coursedb.getCourseCategoryList()
