class Student:
    def __init__(self, name, cls, id):
        self.name = name
        self.id = id
        self.cls = cls

    def __repr__(self) -> str:
        return f'Student Name: {self.name}, Class: {self.cls}, ID: {self.id}'

class Teacher:
    def __init__(self, name, sub, id):
        self.name = name
        self.sub = sub
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher Name: {self.name}, Subject: {self.sub}, ID: {self.id}'

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'c', id)
            self.students.append(student)
            return f'{name} is enrolled with ID {id}, extra money: {fee - 6500}'

    def __repr__(self) -> str:
        result = f'Welcome to the {self.name}\n'
        result += '_______Our Teachers_________\n'
        for teacher in self.teachers:
            result += str(teacher) + '\n'
        result += '______Our Students______\n'
        for student in self.students:
            result += str(student) + '\n'
        return result

# Rest of your code remains the same

phitron = School('Phitron')
phitron.enroll('Seaum', 4000)
phitron.enroll('Badhon', 8000)
phitron.enroll('Sraboni', 5000)
phitron.enroll('Abir', 6500)

phitron.add_teacher('Tom Cruise', 'DS')
phitron.add_teacher('Badhon', 'Algorithm')
phitron.add_teacher('Akash', 'CPP')

print(phitron)
