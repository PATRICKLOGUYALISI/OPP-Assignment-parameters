class Student:
    
    
    
    
    def __init__(self, name, registration_number):
        self.name = name
        self.registration_number = registration_number

    def __str__(self):
        return(f"Student Name: {self.name} Registration Number: {self.registration_number}")
        




student1 = Student("Joshua Kalimba", "REG S23B13/001")
print(student1)

student2 = Student("Ricky Oromo", "REG S23B13/055")
print(student2)

student3 = Student("patrick Loguya", "REG S23B13/095")
print(student3)

student4 = Student("Elizabeth Nanteza", "REG S23B13/122")
print(student4)
