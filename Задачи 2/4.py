class Nikola:
    def __init__(self, name, age):
        if name == 'Николай':
            self.name = name
        else:
            self.name = 'Я не ' + name + ', а Николай'
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
