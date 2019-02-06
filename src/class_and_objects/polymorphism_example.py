class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name
        # "__" prefixed identifier is replaced with _classname__rate when used in a class context
        # It's called name mangling enforced by python interpreter. Python will not import these
        self.__rate = 20.00

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee,self).calculate_wage(hours)


milton  = PartTimeEmployee("Milton")
print(dir(milton))  # _Employee__rate added as a result of name mangling
print(dir(milton._Employee__rate))  # _Employee__rate could be printed at runtime.
print (milton.calculate_wage(10))  # wage calculated as a part time employee
print (milton.full_time_wage(10))  # wage calculated as a full time employee
