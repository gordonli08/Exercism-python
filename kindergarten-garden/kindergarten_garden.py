plant_lookup = {
    'C':'Clover',
    'G':'Grass',
    'R':'Radishes',
    'V':'Violets'
}

defaultStudents = [
    'Alice', 'Bob', 'Charlie', 'David',
    'Eve', 'Fred', 'Ginny', 'Harriet',
    'Ileana', 'Joseph', 'Kincaid', 'Larry'
]

class Garden:

    def __init__(self, diagram, students=None):
        if not students:
            students = defaultStudents.copy()
        else:
            students = sorted(students)
        
        self.student_plants = {}

        row_1, row_2 = diagram.splitlines()
        plants = [row_1[index:index+2]+row_2[index:index+2] for index in range(0,len(row_1),2)]

        for plantgroup in plants:
            person = students.pop(0)
            self.student_plants[person] = [plant_lookup[plant] for plant in plantgroup]

    def plants(self,student):
        return self.student_plants[student]
