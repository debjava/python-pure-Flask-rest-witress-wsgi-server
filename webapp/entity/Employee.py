class Employee:
    empId = None
    firstName = None
    lastName = None

    def __str__(self):
        return str(self.empId) + " " + self.firstName + " " + self.lastName
