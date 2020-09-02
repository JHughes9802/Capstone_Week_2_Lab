from dataclasses import dataclass

@dataclass
class Student:
    # I don't know if I should feel weirded out or comforted by
    # needing to declare data types for variables in Python.
    # Furthermore, I'm curious why the datatype comes AFTER the
    # variable AND why the variable needs a colon after itself.
    name: str
    school_id: int
    gpa: float
    
    # It's interesting that, while above doesn't require the "self" invocation,
    # the return statement here needs it. I'm assuming this is mainly because we're
    # overriding what's built-in, but I'm curious to find out more regarding this topic.
    def __str__(self):
        return f'Student name: {self.name}, ID: {self.school_id}, current GPA: {self.gpa}'

# Fake data to test output, it runs the same as before changing things to use dataclass.
# I made the "school_id" an integer (like our tech IDs) to show that int also works perfectly fine.
def main():
    student1 = Student('Joe', 68413099, 3.4)
    student2 = Student('Tina', 81437270, 3.6)
    student3 = Student('Hank', 14742965, 3.3)
    
    print(student1)
    print(student2)
    print(student3)

main()