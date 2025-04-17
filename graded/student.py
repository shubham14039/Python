class Student:
    count = 0
    def __init__(self, name, roll, maths, physics, chemistry):
        Student.count += 1
        self.roll = roll
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

class Group:
    def __init__(self):
        self.members = [ ]

    def add(self, student):
        self.members.append(student)

    def print_members(self):
        for student in self.members:
            print(student.name)


Student.count = 0
f = open('scores.csv', 'r')
f.readline()	# ignore the header
students = [ ]
for line in f:
    roll, name, maths, physics, chemistry = line.strip().split(',')
    roll, maths, physics, chemistry = int(roll), int(maths), int(physics), int(chemistry)
    students.append(Student(name, roll, maths, physics, chemistry))
f.close()
print(Student.count)
