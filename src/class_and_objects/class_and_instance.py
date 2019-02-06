import datetime


class Employee:

    _total_employees = 0 # private variable.
    raise_percentage = 1.04  # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # "_" postfix is conventionally to resolve name conflict.
        self.date_ = str(datetime.date.today())
        Employee._total_employees += 1

    @classmethod # factory method
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first,last,pay)

    @property  # getter
    def fullName(self):
        return "{0} {1}".format(self.first, self.last)

    @fullName.setter  # setter
    def fullName(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    def pay(self):
        return self.pay()

    def give_raise(self):
        self.pay = int(self.pay * self.raise_percentage)

    @classmethod  # class method has class as parameter
    def total_employees(cls):
        return cls._total_employees

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

    def __repr__(self):
        return "Employee - Representation ('{0}','{1}')".format(self.first, self.last)

    def __str__(self):
        return "{0}-{1}".format(self.first, self.last)

    def __len__(self):
        return len(self.fullName)


if __name__ == "__main__":

    # Constructor
    employee_david = Employee("david", "atten", 40000)
    employee_brad = Employee("brad", "pret", 50000)
    employee_josh = Employee.from_string("josh-wiggin-80000")  # Factory pattern

    # # call on Class need the exact instance to be passed as parameter
    # print(employee_david.fullName)
    # employee_david.fullName = "davidNew atten"

    ##############################################################
    # Special or Dunder methods
    ##############################################################
    # without special method __repr__ it would return object id like => <__main__.Employee object at 0x7f6aecbf05f8>
    print(repr(employee_david))
    # without dunder method __str__ it would return __repr__.
    print(str(employee_david))  # print(employee_david) is same as print(str(employee_david))
    # without special method __len__ this line will throw exception
    print(len(employee_david))
    # Class variable are visible only in class descriptor and not in instance descriptor
    print(Employee.__dict__)
    print(employee_david.__dict__)

    ##############################################################
    # Using Class Variable
    ##############################################################
    print("Before raise {0} ".format(employee_david.pay))
    employee_david.give_raise();
    print("After 4% raise {0}".format(employee_david.pay));


    ##############################################################
    # Class Method
    ##############################################################
    print("Total employee : {0} ".format(Employee.total_employees()))


    ##############################################################
    # Static Method from instance and class
    ##############################################################
    myDate = datetime.date(2016,7,10);
    print(employee_brad.is_workday(myDate))
    print(Employee.is_workday(myDate))
