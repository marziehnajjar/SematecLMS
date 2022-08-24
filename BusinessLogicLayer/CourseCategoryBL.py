from Model import *
from DataAccessLayer import *


class CourseCategoryVD:
    def __init__(self, courseCategory: CourseCategoryModel.CourseCategory):
        self.CourseCategory = courseCategory

    def validationForm(self):
        error = 0

        if error == 0:
            coursecategorydb = CourseCategoryDB(self.coutsecategory)
            coursecategorydb.insertCourseCategory()
