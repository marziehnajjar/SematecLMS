class Employee:
    def __init__(self, managerCode, departmentID, firstName, lastName, nationalCode, sex=None, birthdate=None,
                 email=None, mobile=None, address=None, education=None, hiredate=None):
        self.FirstName = firstName
        self.LastName = lastName
        self.NationalCode = nationalCode
        self.Sex = sex
        self.Birthdate = birthdate
        self.Email = email
        self.Mobile = mobile
        self.Address = address
        self.Education = education
        self.DepartmentID = departmentID
        self.Hiredate = hiredate
        self.ManagerCode = managerCode
