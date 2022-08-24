class Employee:
    def __init__(self, managerID, departmentID, firstName, lastName, nationalCode, sex=None, birthdate=None,
                 email=None, mobile=None, address=None, registerDate=None, educationDegree=None, educationField=None,
                 hiredate=None, photo=None, jobLevelID=None):
        self.FirstName = firstName
        self.LastName = lastName
        self.NationalCode = nationalCode
        self.Sex = sex
        self.Birthdate = birthdate
        self.Email = email
        self.Mobile = mobile
        self.Address = address
        self.RegisterDate = registerDate
        self.EducationDegree = educationDegree
        self.EducationField = educationField
        self.DepartmentID = departmentID
        self.Hiredate = hiredate
        self.ManagerID = managerID
        self.Photo = photo
        self.JobLevelID = jobLevelID
