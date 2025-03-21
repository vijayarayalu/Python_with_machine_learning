"""   Question 2: Student Marks Processing and File Handling 
Steps: 
1. Define calculate_average(marks):  
o Check if the list is empty and raise ValueError. 
o Validate that all elements are numbers; if not, raise TypeError. 
o Compute the average. 
2. Define save_marks_to_file(filename, marks):  
o Open the file in write mode. 
o Write marks to the file. 
o Handle potential IOError. 
3. Define read_marks_from_file(filename):  
o Open the file in read mode. 
o Read marks and convert them to integers. 
o Handle FileNotFoundError and ValueError. 
Example:  
student_marks = [85, 90, 78] 
avg = calculate_average(student_marks) 
print("Average Marks:", avg) 
save_marks_to_file("marks.txt", student_marks) 
read_marks = read_marks_from_file("marks.txt") 
print("Read Marks:", read_marks) 
Output: 
Average Marks: 84.33333333333333 
Read Marks: [85, 90, 78] """

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        if not self.marks:
            raise ValueError("Marks list cannot be empty.")
        if not all(isinstance(m, (int, float)) for m in self.marks):
            raise TypeError("All elements must be numbers.")
        return sum(self.marks) / len(self.marks)

    def save_marks_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(",".join(map(str, self.marks)))

    @staticmethod
    def read_marks_from_file(filename):
        try:
            with open(filename, "r") as file:
                return [int(m) for m in file.read().strip().split(",")]
        except (FileNotFoundError, ValueError):
            return []


student = Student("John", [85, 90, 78])
print(f"Average Marks: {student.calculate_average()}")
student.save_marks_to_file("marks.txt")
print(f"Read Marks: {Student.read_marks_from_file('marks.txt')}")
