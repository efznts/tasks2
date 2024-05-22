class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = {}

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        if subject in self.subjects:
            del self.subjects[subject]

    def average(self):
        if self.subjects:
            average = sum(self.subjects.values()) / len(self.subjects)
            return average
        else:
            return 0
