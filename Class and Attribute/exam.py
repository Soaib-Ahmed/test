class Exam:
    def __init__(self, class_name):
        self.class_name = class_name
        self.attendance = {}
        self.marks = {}

    def take_attendance(self, student_name, present=True):
        if student_name not in self.attendance:
            self.attendance[student_name] = []
        self.attendance[student_name].append(present)

    def record_marks(self, student_name, subject, marks_obtained):
        if student_name not in self.marks:
            self.marks[student_name] = {}
        self.marks[student_name][subject] = marks_obtained

    def get_attendance(self, student_name):
        if student_name in self.attendance:
            return self.attendance[student_name]
        return []

    def get_marks(self, student_name):
        if student_name in self.marks:
            return self.marks[student_name]
        return {}


# Example usage:
math_exam = Exam('Math Class')

math_exam.take_attendance('Alice', present=True)
math_exam.take_attendance('Bob', present=False)
math_exam.take_attendance('Charlie', present=True)

math_exam.record_marks('Alice', 'Math', 90)
math_exam.record_marks('Bob', 'Math', 75)
math_exam.record_marks('Charlie', 'Math', 85)

print(f"Attendance for Alice: {math_exam.get_attendance('Alice')}")
print(f"Marks for Alice in Math: {math_exam.get_marks('Alice')}")

print(f"Attendance for Bob: {math_exam.get_attendance('Bob')}")
print(f"Marks for Bob in Math: {math_exam.get_marks('Bob')}")

print(f"Attendance for Charlie: {math_exam.get_attendance('Charlie')}")
print(f"Marks for Charlie in Math: {math_exam.get_marks('Charlie')}")
