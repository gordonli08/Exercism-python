class School:
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        if grade in self.grades:
            self.grades[grade].append(name)
        else:
            self.grades[grade] = [name]
        self.grades[grade].sort()

    def roster(self):
        return sum([students for grade, students in sorted(self.grades.items())], [])
        
    def grade(self, grade_number):
        if grade_number not in self.grades:
            return []
        return self.grades[grade_number]
