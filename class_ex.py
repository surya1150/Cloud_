class Class_ex:
    def __init__(self,name,rollno,Grade):
        self.name = name
        self.rollno = rollno
        self.Grade = Grade

    def print_details(self):
        print('Name:', self.name)
        print('Rollno:', self.rollno)
        print ('Grade:', self.Grade)


ce = Class_ex("surya",101,"A")
ce.print_details()

