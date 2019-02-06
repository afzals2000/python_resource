class User(object):

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f'{self.name } - {self.height}'

    def __lt__(self, other):
        return self.name < other.name
