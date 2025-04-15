from statistics import mean


class Student:
    def __init__(self, name, age, subject, marks):
        self.name = name
        self.age = age
        self. subject = subject
        self.marks = marks
        
    def avg(self, *marks):
        average = mean(marks)
        
        def grade():
            if average >= 80:
                return ("A")
            elif average > 60:
                return ("B") 
            elif average >= 35:
                return ("C")
            else:
                return("Fail🥲") 
                
        print("----- Student grace book ----")
        print("Student added: ", "Name -", self.name, "Age -", self.age )  
        print("Marks: ", marks)
        print("Average marks: ", int(average))
        print(f"Grade: ",grade())

        
st = Student('malih', 20, 'maths', 80)
st.avg(80,70,90)

        