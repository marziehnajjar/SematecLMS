class Student:
    def __init__(self, studentID=None, firstName=None, lastName=None, nationalCode=None, sex=None, birthdate=None,
                 email=None, mobile=None, country=None, province=None, city=None, street=None, postalcode=None,
                  educationDegree=None, educationField=None, type=None,registerDate=None,):
        self.StudentID = studentID
        self.FirstName = firstName
        self.LastName = lastName
        self.NationalCode = nationalCode
        self.Sex = sex
        self.Birthdate = birthdate
        self.Email = email
        self.Mobile = mobile
        self.Country = country
        self.Province = province
        self.City = city
        self.Street = street
        self.Postalcode = postalcode
        self.RegisterDate = registerDate
        self.EducationDegree = educationDegree
        self.EducationField = educationField
        self.Type = type
