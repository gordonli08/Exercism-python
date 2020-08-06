from collections import defaultdict

class School:
    def __init__(self):
        self.grades = defaultdict(list)

    def add_student(self, name, grade):
        self.grades[grade].append(name)
        self.grades[grade].sort()

    def roster(self):
        return sum([students for grade, students in sorted(self.grades.items())], [])
        
    def grade(self, grade_number):
        if grade_number not in self.grades:
            return []
        return self.grades[grade_number]
