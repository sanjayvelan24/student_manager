# Task 1 — student.py
# Create a Student class with:

# Private attributes: __name, __marks (out of 100)
# Getters for both
# A method get_grade() that returns:

# "A" if marks ≥ 80
# "B" if marks ≥ 60
# "C" if marks ≥ 40
# "F" otherwise


# A to_dict() method that returns the student as a dictionary


class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks
    
    #det = {}
    def to_dict(self):
        return {"name": self.__name, "marks": self.__marks, "grade":self.get_grade()}

    def get_grade(self):
        if self.__marks >= 80 :
            return"A"
        elif self.__marks >=60:
            return"B"
        elif self.__marks >=40:
            return"C"
        else:
            return"F"
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks
    
# result = Student("sanjay", 45)
# print(result.get_grade())
# print(result.get_marks())
# print(result.get_name())
# print(result.to_dict())

